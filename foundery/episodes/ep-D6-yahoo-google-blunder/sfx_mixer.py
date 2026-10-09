"""
sfx_mixer.py — Audio & Sound Design Engine for Episode D6: "The $1M Blunder".
Default: Clean Voice Narration Mode with broadcast compression (-15.5 dB mean volume).
Zero background music / zero background SFX per taste mandate.
"""
import os, sys, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
VOICE_PATH = os.path.join(HERE, 'voice.wav')
OUT_PATH = os.path.join(HERE, 'build', 'out_mix.wav')
VISUAL_MASTER = os.path.join(HERE, 'build', 'visual_master.mp4')
FINAL_MASTER = os.path.join(HERE, 'master_episode_d6.mp4')

print("[SoundDesigner] Running in CLEAN VOICE NARRATION mode (zero background audio / no sfx)...")
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

print(f"[SoundDesigner] Successfully rendered audio: {OUT_PATH}")

# Auto-mux into FINAL_MASTER if visual master exists
if os.path.exists(VISUAL_MASTER):
    print(f"[SoundDesigner] Muxing video with clean narration into {FINAL_MASTER}...")
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
    mux_res = subprocess.run(mux_cmd, capture_output=True, text=True)
    if mux_res.returncode != 0:
        print("Muxing Error:", mux_res.stderr)
        raise RuntimeError("Video-Audio muxing failed")
    print(f"[SoundDesigner] Master video updated successfully: {FINAL_MASTER}")
else:
    print(f"[SoundDesigner] Visual master not found at {VISUAL_MASTER}. Audio ready for muxing.")

