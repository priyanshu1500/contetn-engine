"""
make_voice.py — High-Fidelity Narration & Word-Level Timing Engine for Episode D6: "The $1M Blunder".
Uses native Edge-TTS WordBoundary telemetry for sub-millisecond word sync,
followed by broadcast-standard audio mastering (highpass, compressor, loudnorm).
"""
import asyncio, os, json, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
TEXT_PATH = os.path.join(HERE, 'narration.txt')
TEXT = open(TEXT_PATH, encoding='utf-8').read().strip()
VOICE = 'en-US-ChristopherNeural'
RATE = '+3%'

RAW_PATH = os.path.join(HERE, 'raw_tts.mp3')
VOICE_PATH = os.path.join(HERE, 'voice.wav')
TIMING_PATH = os.path.join(HERE, 'words_timing.json')

async def generate():
    print(f"[VoiceEngine] Synthesizing speech with {VOICE} ({RATE})...")
    import edge_tts
    comm = edge_tts.Communicate(TEXT, VOICE, rate=RATE, boundary="WordBoundary")
    
    words_data = []
    audio_chunks = []
    
    async for chunk in comm.stream():
        if chunk["type"] == "audio":
            audio_chunks.append(chunk["data"])
        elif chunk["type"] == "WordBoundary":
            text = chunk["text"].strip()
            # offset and duration in 100ns units -> seconds
            start = round(chunk["offset"] / 10_000_000, 3)
            dur = round(chunk["duration"] / 10_000_000, 3)
            end = round(start + dur, 3)
            words_data.append({
                "word": text,
                "start": start,
                "end": end,
                "prob": 1.0
            })
            
    with open(RAW_PATH, "wb") as f:
        f.write(b"".join(audio_chunks))
    print(f"[VoiceEngine] Raw audio written: {RAW_PATH}")
    
    # Save exact word timestamps
    with open(TIMING_PATH, "w", encoding="utf-8") as f:
        json.dump(words_data, f, indent=2)
    print(f"[VoiceEngine] Extracted {len(words_data)} native word boundaries to {TIMING_PATH}")

asyncio.run(generate())

print("[VoiceEngine] Mastering broadcast voice chain (compression + loudness normalization)...")
af = 'highpass=f=80,bass=g=3:f=110:w=0.6,acompressor=threshold=-18dB:ratio=3.5:attack=15:release=100,loudnorm=I=-16:TP=-1.5:LRA=10'
subprocess.run(['ffmpeg', '-y', '-i', RAW_PATH, '-af', af, VOICE_PATH], check=True)

dur = subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', VOICE_PATH]).decode().strip()
print(f"[VoiceEngine] Mastered broadcast voice.wav ready: {dur}s")

