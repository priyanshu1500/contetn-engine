# REPLICATION GUIDE: Setting Up the Content Engine on a New PC

> **Purpose:** Step-by-step manual to clone, configure, and operate this autonomous content creation engine on a brand-new computer (Windows, macOS, or Linux) with 100% fidelity.

---

## 1. Prerequisites & System Requirements

Before running the engine, ensure the following core tools are installed and accessible in your system terminal:

### A. Core Software Checklist
| Tool | Recommended Version | Verification Command | Notes |
|---|---|---|---|
| **Python** | 3.10+ (tested on 3.11, 3.12) | `python --version` or `py -3 --version` | Standard library + PIP |
| **Node.js** | 18+ LTS or 20+ LTS (tested on Node v20/v24) | `node -v` | Required for Remotion bundler |
| **FFmpeg / FFprobe**| 6.0+ (tested on 7.x/8.x) | `ffmpeg -version` | **Must be in system PATH** |
| **Git** | Latest | `git --version` | Source control |

---

## 2. Step-by-Step Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/priyanshu1500/contetn-engine.git
cd contetn-engine
```

### Step 2: Install Node Dependencies (Remotion Engine)
Navigate to the engine directory and install the rendering dependencies:
```bash
cd foundery/engine
npm install
cd ../..
```
*Dependencies installed:* `remotion`, `@remotion/bundler`, `@remotion/renderer`, `react`, `react-dom`, `typescript`.

### Step 3: Install Python Dependencies
Install the required audio and transcription libraries:
```bash
pip install Pillow edge-tts faster-whisper
```
*(Optional for YouTube footage curation: `pip install yt-dlp`)*

### Step 4: Configure Chrome Headless Shell (for Remotion)
Remotion uses Chrome Headless Shell for fast server-side rendering.
- By default, Remotion will automatically download a compatible Chrome shell into your local cache upon first render.
- If you have an existing Chrome installation or headless binary, you can set the environment variable:
  ```bash
  # Windows PowerShell:
  $env:CHROME_PATH = "C:\Path\To\chrome-headless-shell.exe"
  # macOS / Linux:
  export CHROME_PATH="/path/to/chrome-headless-shell"
  ```

---

## 3. Directory Structure Overview

```
contetn-engine/
├── AGENTS.md                       # Protocol & taste mandates for AI agents
├── SYSTEM_KNOWLEDGE_BASE.md        # Technical specifications & typography tokens
├── VENTURES.md                     # Foundery (B2B AI) vs LexIntent (student resume)
├── guidebooks/                     # Complete SOPs & thoughtprocess documentation
│   ├── REPLICATION_GUIDE_NEW_PC.md # This setup file
│   ├── THOUGHT_PROCESS_AND_RESEARCH.md # Reference breakdown & evolution history
│   ├── METROMEDIA_EDITORIAL_PLAYBOOK.md # Frame-by-frame rhythm & shot archetypes
│   ├── DESIGN_PHILOSOPHY.md        # Brand guidelines & camera rules
│   ├── PIPELINE.md                 # Master build SOP
│   └── QC_CHECKLIST.md             # Pre-flight QC validation
├── references/                     # Reference montages & master contact sheets
├── foundery/                       # Foundery AI Agency System
│   ├── engine/                     # Remotion engine (DocReel.tsx, theme.ts, render.mjs)
│   ├── episodes/                   # Production episodes (e.g. ep-D4-500b-living-room)
│   └── demos/                      # Node mascot & SaaS demo reels
├── lexintent/                      # LexIntent Student & Law Platform System
│   ├── dossiers/                   # Research dossiers & competitive analysis
│   ├── scripts_and_plans/          # Hook formulas & growth engines
│   └── voice/                      # Indian-accent voice selection tools
└── assets/                         # Core fonts, sound effects, and music beds
```

---

## 4. How to Render an Existing Episode (Benchmark Test)

To verify your installation, render **Episode D4 ("The Fake Account Empire — The Reddit Origin Story")**:

### 1. Build the Edit Decision List (EDL):
```bash
cd foundery/episodes/ep-D4-500b-living-room
python build_edl.py
```
*Output:* Creates `build/edl.json` containing 18 shots and 80 multi-font kinetic caption tracks.

### 2. Render Key Stills (Quick Visual Verification):
```bash
node ../../engine/render.mjs stills build/edl.json build/public ../../stills_test 60,521,659
```
*Verification:*
- `f_0060.png`: Iconic YC 2005 class photo punch.
- `f_0521.png`: Stark pure-white optical reset slide with black captions.
- `f_0659.png`: Elevated taped Polaroid with handwritten cursive script.

### 3. Render Visual Video:
```bash
node ../../engine/render.mjs video build/edl.json build/public build/visual_master.mp4
```

### 4. Build Master Audio Mix:
```bash
python sfx_mixer.py
```
*Output:* Generates `build/out_mix.wav` with broadcast loudness compression (`-15.7 dB mean volume`).

### 5. Mux Master Video:
```bash
ffmpeg -y -i build/visual_master.mp4 -i build/out_mix.wav -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 256k -shortest master_episode_d4.mp4
```

### 6. Verify Broadcast Loudness:
```bash
ffmpeg -i master_episode_d4.mp4 -af "volumedetect" -vn -sn -dn -f null NUL
```
*Target:* `mean_volume` must be between `-14.0 dB` and `-16.5 dB`, with peak between `-0.5 dB` and `-0.0 dB`.

---

## 5. How to Create a Brand New Episode

### Step 1: Draft the Narration Script
Create a new folder under `foundery/episodes/ep-XXX-your-title/` and write `narration.txt`:
- Use high-status documentary writing (no generic sales pitch).
- Focus on tension, contradiction, and primary proof.

### Step 2: Generate Voice & Word Timings
```python
# make_voice.py
import edge_tts, asyncio, subprocess
TEXT = open("narration.txt", encoding="utf-8").read()
asyncio.run(edge_tts.Communicate(TEXT, "en-US-ChristopherNeural", rate="+3%").save("raw_tts.mp3"))
af = 'highpass=f=80,bass=g=3:f=110:w=0.6,acompressor=threshold=-18dB:ratio=3.5:attack=15:release=100,loudnorm=I=-16:TP=-1.5:LRA=10'
subprocess.run(['ffmpeg', '-y', '-i', 'raw_tts.mp3', '-af', af, 'voice.wav'], check=True)
```
Extract word timings with `faster-whisper` into `words_timing.json`.

### Step 3: Source Real Archival Assets
- Download authentic clips/photos using `yt-dlp` or public domain archives.
- Save 1920x1080 assets in `build/public/clips/` and `build/public/img/`.
- **STRICT BAN:** Never use generic AI mockups or repeating ChatGPT frames.

### Step 4: Assemble `build_edl.py`
Map out shots and let `editorial_edl.py` automatically route typography:
- Numbers $\rightarrow$ `displayCondensed` with yellow highlight box.
- Emotional words $\rightarrow$ `serifItalic` (Playfair Display).
- Technical terms $\rightarrow$ `mono` (IBM Plex Mono).
- Standard text $\rightarrow$ clean `sans` (Inter).

### Step 5: Render & QC
Follow the render and mux commands above, then run the QC Checklist in `guidebooks/QC_CHECKLIST.md`.

---

## 6. Troubleshooting Common Issues

### Issue 1: "Voiceover is too quiet in final mix"
- **Cause:** Using ffmpeg `amix` without `:normalize=0`. Default ffmpeg `amix` divides every track by `1/N`.
- **Fix:** In `sfx_mixer.py`, ensure:
  `amix=inputs=N:duration=first:dropout_transition=2:normalize=0,volume=1.15,alimiter=limit=0.98:attack=2:release=50`

### Issue 2: "Chrome Headless Shell not found"
- **Fix:** Set `$env:CHROME_PATH` to your local Chrome or let Remotion download it:
  `npx remotion install chrome-headless-shell`

### Issue 3: "White caption invisible on white slide"
- **Fix:** Pass `dark_intervals=[(t_start, t_end)]` into `format_caption_chunks()` in `build_edl.py`. The engine will automatically render dark `#0A0A0A` text on light backgrounds.

