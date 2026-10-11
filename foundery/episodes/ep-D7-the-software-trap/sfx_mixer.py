import os, subprocess

# Paths
EP_DIR = r"D:\agency content\BIN\documentary_tofu\ep-D7-the-software-trap"
VISUAL_MASTER = os.path.join(EP_DIR, "build", "visual_master.mp4")
VOICE_PATH = os.path.join(EP_DIR, "voice.wav")
CNBC_BITE = os.path.join(EP_DIR, "cnbc_bite_loud_final.wav")
FINAL_OUT = os.path.join(EP_DIR, "master_episode_d7.mp4")

# Sound design elements
# 1. Voiceover ( ChristopherNeural at -16dB )
# 2. News soundbite intercut ( CNBC anchor from 49.5s to 54.5s at -16dB )
#    We duck the voice track during 49.5s to 54.5s, or blend seamlessly.
# 3. Cinematic subtle documentary drone / low rumble
# 4. Filter graph using complex amix (normalize=0) and alimiter

print("[SFX Mixer] Starting master audio assembly for Episode D7...")

# Audio filter graph:
# [0:a] is voice.wav
# [1:a] is cnbc_bite_loud_final.wav delayed by 49500ms (49.5s)
# During 49.5s to 54.5s, voice is naturally sparse, but we apply volume ducking:
# voice volume drops by 12dB between 49.5 and 54.5 to let the CNBC bite pierce cleanly.

filter_complex = (
    "[0:a]volume='if(between(t,49.5,54.5),0.25,1.0)':eval=frame[v_duck]; "
    "[1:a]adelay=49500|49500[cnbc_del]; "
    "[v_duck][cnbc_del]amix=inputs=2:duration=first:normalize=0,"
    "volume=1.05,alimiter=limit=0.98:attack=2:release=50[aout]"
)

cmd = [
    "ffmpeg", "-y",
    "-i", VISUAL_MASTER,
    "-i", VOICE_PATH,
    "-i", CNBC_BITE,
    "-filter_complex",
    "[1:a]volume='if(between(t,49.5,54.5),0.25,1.0)':eval=frame[v_duck]; "
    "[2:a]adelay=49500|49500[cnbc_del]; "
    "[v_duck][cnbc_del]amix=inputs=2:duration=first:normalize=0,"
    "volume=1.05,alimiter=limit=0.98:attack=2:release=50[aout]",
    "-map", "0:v",
    "-map", "[aout]",
    "-c:v", "copy",
    "-c:a", "aac",
    "-b:a", "320k",
    "-shortest",
    FINAL_OUT
]

print("Command prepared. Run when visual master completes.")
if __name__ == "__main__":
    if os.path.exists(VISUAL_MASTER):
        print("Running ffmpeg master audio mix...")
        subprocess.run(cmd, check=True)
        print("Master episode complete:", FINAL_OUT)
        # Check volume
        chk = subprocess.run(["ffmpeg", "-i", FINAL_OUT, "-af", "volumedetect", "-vn", "-sn", "-dn", "-f", "null", "NUL"], capture_output=True, text=True)
        for line in chk.stderr.splitlines():
            if "mean_volume" in line or "max_volume" in line:
                print(line)
    else:
        print("Visual master still rendering...")

