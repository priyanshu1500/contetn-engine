import asyncio
import json
import os
import subprocess
import edge_tts

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
NARRATION_PATH = os.path.join(ROOT_DIR, "narration.json")
LINES_DIR = os.path.join(ROOT_DIR, "lines")
OUTPUT_VO = os.path.join(ROOT_DIR, "vo.mp3")
CAPTIONS_OUTPUT = os.path.join(os.path.dirname(ROOT_DIR), "captions.json")

async def generate_cue_audio(cue_id, text, voice, rate, out_mp3, out_vtt):
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    submaker = edge_tts.SubMaker()
    with open(out_mp3, "wb") as file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                submaker.feed(chunk)
    with open(out_vtt, "w", encoding="utf-8") as file:
        file.write(submaker.get_srt())

def get_audio_duration(file_path):
    cmd = [
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", file_path
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return float(result.stdout.strip())

async def main():
    with open(NARRATION_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    voice = data.get("voice", "en-US-AndrewMultilingualNeural")
    rate = data.get("rate", "+8%") # Energetic top-creator pacing
    cues = data.get("cues", [])
    
    os.makedirs(LINES_DIR, exist_ok=True)
    
    cue_metadata = []
    current_time = 0.25 # Crisp opening hook entry at 0.25s
    
    for idx, cue in enumerate(cues):
        cid = cue["id"]
        text = cue["text"]
        mp3_path = os.path.join(LINES_DIR, f"line_{cid:02d}.mp3")
        vtt_path = os.path.join(LINES_DIR, f"line_{cid:02d}.vtt")
        
        print(f"Generating voice for Cue {cid}...")
        await generate_cue_audio(cid, text, voice, rate, mp3_path, vtt_path)
        
        duration = get_audio_duration(mp3_path)
        start_t = current_time
        end_t = start_t + duration
        
        cue_info = {
            "id": cid,
            "header_1": cue["header_1"],
            "header_2": cue["header_2"],
            "progress_state": cue["progress_state"],
            "text": text,
            "start": round(start_t, 2),
            "end": round(end_t, 2),
            "duration": round(duration, 2),
            "mp3": mp3_path,
            "vtt": vtt_path
        }
        cue_metadata.append(cue_info)
        current_time = end_t + 0.3 # 0.3s snappy breathing space
        
    print("Mastering final VO with Broadcast Compression + EBU R128 (-14 LUFS)...")
    
    # Mix with adelay and normalize=0 (NO volume attenuation)
    filter_complex = []
    inputs = []
    for i, cm in enumerate(cue_metadata):
        inputs.extend(["-i", cm["mp3"]])
        filter_complex.append(f"[{i}:a]adelay={int(cm['start']*1000)}|{int(cm['start']*1000)}[a{i}];")
        
    mix_inputs = "".join(f"[a{i}]" for i in range(len(cue_metadata)))
    # normalize=0 prevents amix from dropping volume by 1/N!
    filter_complex.append(f"{mix_inputs}amix=inputs={len(cue_metadata)}:duration=longest:dropout_transition=0:normalize=0[raw_mix];")
    
    # Broadcast Master Chain:
    # 1. highpass at 75Hz (removes low-end rumble)
    # 2. compand (tight vocal compression for upfront presence)
    # 3. loudnorm (locks integrated loudness to -14.0 LUFS with -1.0 dBTP true peak)
    master_chain = (
        "[raw_mix]highpass=f=75,"
        "compand=attacks=0.02:decays=0.1:points=-80/-80|-40/-24|-20/-10|0/-1:gain=3,"
        "loudnorm=I=-14:TP=-1.0:LRA=7[aout]"
    )
    filter_complex.append(master_chain)
    
    cmd_mix = ["ffmpeg", "-y"] + inputs + ["-filter_complex", "".join(filter_complex), "-map", "[aout]", "-b:a", "256k", OUTPUT_VO]
    subprocess.run(cmd_mix, check=True)
    
    total_dur = get_audio_duration(OUTPUT_VO)
    print(f"Master VO generated: {OUTPUT_VO} ({total_dur:.2f} seconds at full -14 LUFS)")
    
    # Save captions and cue boundaries
    with open(CAPTIONS_OUTPUT, "w", encoding="utf-8") as f_cap:
        json.dump({
            "total_duration": total_dur,
            "cues": cue_metadata
        }, f_cap, indent=2)
        
    print(f"Saved captions metadata to {CAPTIONS_OUTPUT}")

if __name__ == "__main__":
    asyncio.run(main())
