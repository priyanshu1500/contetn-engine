import asyncio, subprocess, sys, json, os

HERE = r'D:\agency content\BIN\documentary_tofu\ep-D4-500b-living-room'
TEXT = open(os.path.join(HERE, 'narration.txt'), encoding='utf-8').read()
VOICE = 'en-US-ChristopherNeural'
RAW = os.path.join(HERE, 'raw_tts.mp3')
OUT = os.path.join(HERE, 'voice.wav')
TIMING = os.path.join(HERE, 'words_timing.json')

print("[VoiceEngine] Generating Edge-TTS narration...")
import edge_tts
asyncio.run(edge_tts.Communicate(TEXT, VOICE, rate="+3%").save(RAW))

print("[VoiceEngine] Mastering broadcast voice chain...")
af = 'highpass=f=80,bass=g=3:f=110:w=0.6,acompressor=threshold=-18dB:ratio=3.5:attack=15:release=100,loudnorm=I=-16:TP=-1.5:LRA=10'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', RAW, '-af', af, OUT], check=True)

dur = subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', OUT]).decode().strip()
print(f"[VoiceEngine] Mastered voice.wav: {dur}s")

print("[VoiceEngine] Aligning word-level timestamps with Faster-Whisper...")
sys.path.insert(0, r'D:\agency content\tools')
from metromedia_studio.subtitles_engine import SubtitlesEngine

words = SubtitlesEngine().transcribe_words(OUT, TIMING)
print(f"[VoiceEngine] Extracted {len(words)} aligned words. Last word: '{words[-1]['word']}' at {words[-1]['end']}s")

