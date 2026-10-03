"""
sfx_mixer.py — Layered Audio & Sound Design Engine for Foundery Documentary Reels.
MetroMedia & Next Creatives Standard:
  1. Voice Narration: crisp broadcast compression + EQ (0 dB)
  2. Music Bed: Dark driving cinematic synth/bass bed (-18 dB under voice)
  3. Shot Cut Whooshes: Clean kinetic air whooshes on cuts (-14 dB)
  4. Archival Shutter SFX: Camera click on identity punch-ins (-11 dB)
  5. Sub-Bass Impacts: Heavy sub-drop on stat counters & turning points (-9 dB)
"""
import os, json, subprocess

HERE = r'D:\agency content\BIN\documentary_tofu\ep-D4-500b-living-room'
EDL_PATH = os.path.join(HERE, 'build', 'edl.json')
VOICE_PATH = os.path.join(HERE, 'voice.wav')
OUT_PATH = os.path.join(HERE, 'build', 'out_mix.wav')

SFX_DIR = r'D:\agency content\assets\elements\sfx'
MUSIC_DIR = r'D:\agency content\assets\music'

WHOOSH = os.path.join(SFX_DIR, 'whoosh_427823.mp3')
WHOOSH_ALT = os.path.join(SFX_DIR, 'whoosh_267951.mp3')
IMPACT = os.path.join(SFX_DIR, 'impact_427803.mp3')
SHUTTER = os.path.join(SFX_DIR, 'shutter_676375.mp3')
MUSIC = os.path.join(MUSIC_DIR, 'bed-ccby-423499.mp3')

edl = json.load(open(EDL_PATH, encoding='utf-8'))
total_dur = edl['duration']
shots = edl['shots']

print(f"[SoundDesigner] Building mix for {total_dur}s ({len(shots)} shots)...")

events = []

for idx, s in enumerate(shots):
    t0 = s['t0']
    kind = s.get('kind', '')
    job = s.get('job', '')
    
    # Whoosh on cut transitions
    if idx > 0 and t0 < total_dur - 1.0:
        w_file = WHOOSH_ALT if idx % 2 == 0 else WHOOSH
        events.append({'time': t0, 'file': w_file, 'vol': 0.22, 'tag': f'whoosh_s{idx+1}'})
    
    # Shutter click on photo punch-ins
    if 'punch:' in job or 'photo' in job:
        events.append({'time': t0, 'file': SHUTTER, 'vol': 0.28, 'tag': f'shutter_s{idx+1}'})
        
    # Sub-impact on stat counters and acquisitions
    if kind == 'stat' or 'exit' in job or 'deal' in job or 'quote:' in job:
        events.append({'time': t0, 'file': IMPACT, 'vol': 0.35, 'tag': f'impact_s{idx+1}'})

print(f"[SoundDesigner] Generated {len(events)} dynamic SFX events.")

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

print("[SoundDesigner] Executing FFmpeg audio mix...")
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode != 0:
    print("FFmpeg Error:", res.stderr)
    raise RuntimeError("Audio mix failed")

print(f"[SoundDesigner] Successfully rendered mastered mix: {OUT_PATH}")

