# AGENTS.md: Autonomous Agent Operating Protocol & Taste Mandate

> **Target Audience:** Any autonomous AI agent, pair-programmer, or subagent working in `D:\agency content`.  
> **Mission:** Produce world-class, high-status documentary reels and marketing assets that match or exceed accounts like `@metromedia.house` and `@stanlaunchpad`.

---

## 1. Non-Negotiable Taste Mandates & Strict Bans

Every agent working in this repository must operate with top-tier creative director taste. The following practices are **STRICTLY BANNED**:

### 🚫 The Banned List
1. **NO Generic AI Slop:**
   - Never use a single font centered at the bottom of the screen with yellow word-by-word karaoke highlights across an entire video.
   - Never repeat the same generic UI asset (e.g. standard ChatGPT chatbox, fake terminal frame) across multiple videos. The user explicitly flagged this: *"the assets like the chatgpt window frame etc are getting repeated in every other video that just makes our page look more predictable and fake fix that"*.
2. **NO Low-Volume or Drowned-Out Audio:**
   - Never let narrator voiceover fall below `-16.0 dB mean volume`.
   - Never use ffmpeg `amix` without `:normalize=0`. Default ffmpeg `amix` reduces volume by `1/N` per track, causing the voiceover to become inaudible.
   - User complaint reference: *"the narration should be same way loud as it was in our previous reel dont fuct that volume man"*.
3. **NO Hallucinated Founder Names or Misspellings:**
   - Cross-check all founder names, dates, metrics, and quotes before rendering. Example: *Steve Huffman*, *Alexis Ohanian*, *Paul Graham*, *Sam Altman*, *Jensen Huang*.
4. **NO Monotonous Visual Pacing:**
   - Never hold a static asset or single dark video clip for longer than 3.0 seconds without a motion punch, scale shift, or visual transition.
   - Optical contrast must reset rhythmically: alternate between dark cinematic footage and stark pure-white graphic slides every 1.5–2.5 seconds.

---

## 2. Standard Tooling & Environment Setup

All agents must use the following pre-configured paths and tool invocations:

| Tool | Invocation / Path | Key Flags & Requirements |
|---|---|---|
| **Python** | `python` or `py -3` | Standard library + `Pillow` + `faster-whisper`. Run scripts with full Windows paths or relative to episode folder. |
| **FFmpeg / FFprobe** | `ffmpeg`, `ffprobe` (in system PATH) | Always test audio volume with `-af "volumedetect"`. |
| **Node / Remotion** | `node render.mjs` inside `engine/` | Custom render script using `@remotion/renderer`. |
| **Chrome Headless Shell** | `D:/agency content/.remotion/chrome-headless-shell/win64/chrome-headless-shell-win64/chrome-headless-shell.exe` | Explicitly passed via `--gl=angle` in `render.mjs` for GPU stability on Windows. |
| **OpenCLI / yt-dlp** | `yt-dlp` | For curating real archival footage and founder reference clips. |

---

## 3. Remotion Engine Architecture & Key Modules

When working with video rendering in `D:\agency content\BIN\documentary_tofu\engine\`:

### 1. `src/theme.ts`
- Defines color tokens: `starkWhite: '#FFFFFF'`, `starkBlack: '#060607'`, `highlightYellow: 'rgba(245, 197, 66, 0.65)'`, `tape: 'rgba(240, 235, 220, 0.75)'`.
- Defines typography tokens:
  - `sans`: Inter, SF Pro Display
  - `serifItalic`: Playfair Display Italic
  - `displayCondensed`: Bebas Neue
  - `mono`: IBM Plex Mono
  - `handwritten`: Caveat

### 2. `src/DocReel.tsx`
- Injects Google Web Fonts (`Playfair Display`, `Bebas Neue`, `IBM Plex Mono`, `Caveat`, `Inter`).
- Renders shot archetypes:
  - `video_cinematic`: Letterboxed archival footage with continuous forward camera creep.
  - `stark_slide`: Pure white optical reset graphic slide with high-contrast black typography.
  - `polaroid_card`: Photoreal polaroid paper card with realistic semi-transparent tape and handwritten name tags.
- Renders `WordCap` captions:
  - Dynamically switches font families based on `w.fontKind`.
  - Applies box highlights (`w.box: 'yellow' | 'white'`).
  - Implements kinetic scale punch on entrance.

### 3. `editorial_edl.py`
- Automated NLP entity parser that ingests transcript cues and assigns `fontKind`, `box`, and `rotate` parameters.
- Converts raw numbers $\rightarrow$ `condensed` with `yellow` box.
- Converts power adjectives $\rightarrow$ `serif-italic`.
- Converts technical entities $\rightarrow$ `mono`.

---

## 4. Audio Loudness & Mastering Standards

When generating or mixing audio in `sfx_mixer.py` or ffmpeg:
```python
# Voiceover mastering filter:
vo_filter = "volume=1.45,alimiter=limit=0.98:attack=2:release=50"

# Complex multi-track amix (CRITICAL: normalize=0):
amix_filter = "[1:a]volume=1.35[v]; [2:a]volume=0.85[s]; [3:a]volume=0.18[m]; [v][s][m]amix=inputs=3:duration=first:normalize=0,alimiter=limit=0.98[outa]"
```
**Verification Command:**
```bash
ffmpeg -i output.mp4 -af "volumedetect" -vn -sn -dn -f null NUL
# Verify: mean_volume between -14.0 dB and -16.5 dB, max_volume between -0.1 dB and -0.5 dB
```

---

## 5. Standard Episode Assembly Workflow

To create or update an episode:
1. **Script & Narration:**
   - Draft high-status documentary script in `narration.txt`.
   - Generate speech audio with Edge TTS (`make_voice.py`).
   - Extract word-level timestamps with `faster-whisper` (`clean_timings.py`).
2. **Asset Sourcing & Card Generation:**
   - Download authentic archival footage and founder photos (NO repetitive AI mockups!).
   - Generate bespoke cards (e.g. 2005 Reddit UI in `make_reddit_cards.py`, Paul Graham quote card in `make_pg_card.py`).
3. **EDL Compilation:**
   - Run `build_edl.py` to map shots, visual archetypes, and multi-font captions.
4. **Visual & Still Verification:**
   - Render key stills (`node render.mjs still --frame <N>`).
   - Generate a contact sheet with `ffmpeg tile` to visually inspect typography, contrast, and layout balance.
5. **Master Render & Audio Mix:**
   - Render video (`node render.mjs video`).
   - Run `sfx_mixer.py` to mix broadcast-loud VO, tactile SFX, and ambient soundtrack.
   - Verify final master with `volumedetect`.

---

## 6. Where Knowledge Lives
- `D:\agency content\SYSTEM_KNOWLEDGE_BASE.md`: Deep architectural and creative guide.
- `D:\agency content\BIN\docs\METROMEDIA_EDITORIAL_PLAYBOOK.md`: Frame-by-frame breakdown of the MetroMedia aesthetic.
- `D:\agency content\BIN\docs\DESIGN_PHILOSOPHY.md`: Core agency brand and positioning rules.
- `D:\agency content\BIN\docs\PIPELINE.md`: Technical FFmpeg and Python script specs.

