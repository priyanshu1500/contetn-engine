"""
sfx_mixer.py — Audio & Sound Design Engine for Foundery Documentary Reels.
Supports:
  1. Clean Voice Narration Mode (Default): Broadcast-compressed, EQ'd vocal track with zero background music or sfx.
  2. Full SFX Mix Mode (--full-mix): Multi-track blend with music bed, whooshes, impacts, and shutter clicks.
"""
import os, sys, json, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
EDL_PATH = os.path.join(HERE, 'build', 'edl.json')
RAW_TTS_PATH = os.path.join(HERE, 'raw_tts.mp3')
VOICE_PATH = os.path.join(HERE, 'voice.wav')
OUT_PATH = os.path.join(HERE, 'build', 'out_mix.wav')
VISUAL_MASTER = os.path.join(HERE, 'build', 'visual_master.mp4')
FINAL_MASTER = os.path.join(HERE, 'master_episode_d4.mp4')

SFX_DIR = os.path.normpath(os.path.join(HERE, '..', '..', '..', 'assets', 'elements', 'sfx'))
MUSIC_DIR = os.path.normpath(os.path.join(HERE, '..', '..', '..', 'assets', 'music'))

WHOOSH = os.path.join(SFX_DIR, 'whoosh_427823.mp3')
WHOOSH_ALT = os.path.join(SFX_DIR, 'whoosh_267951.mp3')
IMPACT = os.path.join(SFX_DIR, 'impact_427803.mp3')
SHUTTER = os.path.join(SFX_DIR, 'shutter_676375.mp3')
MUSIC = os.path.join(MUSIC_DIR, 'bed-ccby-423499.mp3')

# Auto-heal voice.wav if missing
if not os.path.exists(VOICE_PATH) and os.path.exists(RAW_TTS_PATH):
    print("[SoundDesigner] voice.wav not found. Generating from raw_tts.mp3 with broadcast mastering...")
    vo_prep = [
        'ffmpeg', '-y', '-i', RAW_TTS_PATH,
        '-af', 'volume=1.45,alimiter=limit=0.98:attack=2:release=50',
        '-c:a', 'pcm_s16le', VOICE_PATH
    ]
    subprocess.run(vo_prep, check=True)

voice_only_mode = '--full-mix' not in sys.argv

if voice_only_mode:
    print("[SoundDesigner] Running in CLEAN VOICE NARRATION mode (zero background audio / no sfx)...")
    # Clean broadcast mastering filter
    cmd = [
        'ffmpeg', '-y', '-i', VOICE_PATH,
        '-af', 'volume=1.35,alimiter=limit=0.98:attack=2:release=50,aformat=sample_rates=48000:channel_layouts=stereo',
        '-c:a', 'pcm_s16le',
        OUT_PATH
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("FFmpeg Error:", res.stderr)
        raise RuntimeError("Clean voice mastering failed")
else:
    print("[SoundDesigner] Running in FULL SFX MIX mode...")
    edl = json.load(open(EDL_PATH, encoding='utf-8'))
    total_dur = edl['duration']
    shots = edl['shots']
    
    events = []
    for idx, s in enumerate(shots):
        t0 = s['t0']
        kind = s.get('kind', '')
        job = s.get('job', '')
        if idx > 0 and t0 < total_dur - 1.0:
            w_file = WHOOSH_ALT if idx % 2 == 0 else WHOOSH
            events.append({'time': t0, 'file': w_file, 'vol': 0.22, 'tag': f'whoosh_s{idx+1}'})
        if 'punch:' in job or 'photo' in job:
            events.append({'time': t0, 'file': SHUTTER, 'vol': 0.28, 'tag': f'shutter_s{idx+1}'})
        if kind == 'stat' or 'exit' in job or 'deal' in job or 'quote:' in job:
            events.append({'time': t0, 'file': IMPACT, 'vol': 0.35, 'tag': f'impact_s{idx+1}'})
    
    cmd = ['ffmpeg', '-y', '-i', VOICE_PATH, '-i', MUSIC]
    for ev in events:
        cmd.extend(['-i', ev['file']])
    
    filter_chains = []
    filter_chains.append("[0:a]volume=1.05,highpass=f=75,lowpass=f=12000,aformat=sample_rates=48000:channel_layouts=stereo[v_clean]")
    filter_chains.append(f"[1:a]atrim=0:{total_dur},volume=0.13,afade=t=in:ss=0:d=1.5,afade=t=out:st={total_dur-2.5}:d=2.5,aformat=sample_rates=48000:channel_layouts=stereo[m_clean]")
    
    mix_inputs = ["[v_clean]", "[m_clean]"]
    for idx, ev in enumerate(events):
        input_idx = idx + 2
        delay_ms = int(ev['time'] * 1000)
        vol = ev['vol']
        tag = f"sfx_{idx}"
        filter_chains.append(f"[{input_idx}:a]adelay={delay_ms}|{delay_ms},volume={vol},aformat=sample_rates=48000:channel_layouts=stereo[{tag}]")
        mix_inputs.append(f"[{tag}]")
    
    all_inputs = "".join(mix_inputs)
    n_inputs = len(mix_inputs)
    filter_chains.append(f"{all_inputs}amix=inputs={n_inputs}:duration=first:dropout_transition=2,volume=1.12,dynaudnorm=f=150:g=15:m=2.0[out_a]")
    
    filter_complex = ";".join(filter_chains)
    cmd.extend([
        '-filter_complex', filter_complex,
        '-map', '[out_a]',
        '-c:a', 'pcm_s16le',
        OUT_PATH
    ])
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("FFmpeg Error:", res.stderr)
        raise RuntimeError("Audio mix failed")

print(f"[SoundDesigner] Successfully rendered audio: {OUT_PATH}")

# Mux final video if visual master exists
if os.path.exists(VISUAL_MASTER):
    print(f"[SoundDesigner] Muxing into {FINAL_MASTER}...")
    mux_cmd = [
        'ffmpeg', '-y',
        '-i', VISUAL_MASTER,
        '-i', OUT_PATH,
        '-map', '0:v:0',
        '-map', '1:a:0',
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-b:a', '256k',
        '-shortest',
        FINAL_MASTER
    ]
    subprocess.run(mux_cmd, check=True)
    print(f"[SoundDesigner] Master video updated successfully: {FINAL_MASTER}")
