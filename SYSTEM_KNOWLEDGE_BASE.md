# SYSTEM KNOWLEDGE BASE: High-Status Documentary & Editorial Video Engine

> **Version:** 3.0 (MetroMedia & StanLaunchpad Editorial Standard)  
> **Last Updated:** 2026-10-03  
> **Maintainer:** Antigravity Autonomous Video Engine  
> **Scope:** Entire `agency content` workspace & all automated documentary/reel pipelines.

---

## 1. Executive Summary & Core Philosophy

This repository builds high-retention, high-status documentary reels and automated video content. The creative direction is modeled after top-tier editorial and founder accounts:
- **`@metromedia.house`**: Archival cinematic documentaries exploring iconic creators (Kubrick, Nolan, Spielberg, Fincher) and high-stakes founders.
- **`@stanlaunchpad`**: High-velocity founder narratives detailing modern bootstrapped and venture-backed outliers ($40M ARR, YC cohorts).

### The Golden Mandate
**Never produce generic "AI video slop".**
Generic social media automation looks like:
- Montserrat or Arial Bold with yellow karaoke highlights pinned to the bottom 20% of the screen.
- Repetitive, generic UI frames (e.g., repeating the same ChatGPT prompt window in every single video).
- Uniform Ken Burns pans with random jitter and artificial camera shake.
- Quiet, muddy narration drowned out by cinematic soundtrack beds.

High-status editorial video looks like:
- **Magazine-level multi-font typography**: Mixing elegant serif italics, punchy condensed metrics, monospace archival stamps, and raw conversational sans.
- **The Optical Contrast Reset ("The Contrast Flip")**: Rhythmically alternating between deep moody archival footage and stark, blinding-white high-key graphic slides every 1.5 to 2.5 seconds to reset the viewer's optic nerve and destroy the scroll reflex.
- **Authentic, bespoke physical artifacts**: Taped Polaroid prints on textured backgrounds, real 2005 Reddit UI archives, authentic IMDb budget sheets with fluorescent highlighter sweeps, and newspaper clippings.
- **Broadcast-standard audio loudness**: Crystal-clear voiceover mastered at `-14.0 dB to -16.0 dB LUFS/mean` with hard compression and zero voice-ducking attenuation.

---

## 2. Forensic Breakdown of Reference Masterclasses

### Reference 1: MetroMedia House (`https://www.instagram.com/p/DbyQ6Vhti_w/`)
- **Hook Thesis:** "Stanley Kubrick, Christopher Nolan, Steven Spielberg... you know their names. You're not one of them."
- **Typography Switching:**
  - Standard speech: Clean, lowercase sans-serif (`you know`, `he was`).
  - Thematic punchlines: High-fashion Serif Italic (`obsession`, `genius`).
  - Hard metrics: Condensed uppercase sans (`70 takes`, `$13 million`).
- **Layout Architecture:**
  - *Frame 1-2:* Archival 35mm film camera behind-the-scenes footage (dark/rich).
  - *Frame 3:* Stark pure white background with small centered Polaroid taped to the frame, handwritten name above.
  - *Frame 9:* High-key white frame with centered 16:9 video tile and split typography flanking left and right (`maybe` [video] `a little`).
  - *Frame 13:* Realistic IMDb budget crop with an animated yellow highlighter sweeping over `$13 million`.
  - *Frame 18:* Tool constellation featuring floating real app badges (Cursor, Replit, Figma, Claude) orbiting a centered thesis statement.

### Reference 2: StanLaunchpad (`https://www.instagram.com/p/Dd9SApxt5JC/`)
- **Hook Thesis:** "Why are these two guys making $40M ARR from a college apartment?"
- **Visual Dynamic:**
  - Contrast flip from outdoor street interview $\rightarrow$ dark CRT scanline screen $\rightarrow$ pure white investor deck tile $\rightarrow$ split-screen co-founder comparison.
  - Floating avatar badges connected with subtle bezier curved tracking lines.
  - Giant condensed currency stamps (`$40M`) punching the screen with scale overshoot.

---

## 3. Typography Architecture & Font Tokens

The system strictly bans monolithic single-font captions. Every caption chunk must be parsed through the multi-font token system:

| Font Kind | Font Family | Weight / Style | Purpose & Emotional Trigger | Example Usages |
|---|---|---|---|---|
| **`sans`** | `Inter`, `SF Pro Display`, system-ui | 500–600 Regular/Medium | Conversational baseline narration; rapid word flow. | `"you know"`, `"built it in"`, `"behind closed doors"` |
| **`serifItalic`**| `Playfair Display`, `Newsreader`, Georgia | 600–700 Italic | Prestige, legacy, deep emotion, obsession, genius, tragedy. | `*obsession*`, `*conviction*`, `*legendary*`, `*instinct*` |
| **`displayCondensed`**| `Bebas Neue`, `Anton`, `Druk` | 800–900 Condensed Extra Bold | Metrics, scale, financial figures, hard quantities, shock numbers. | `"$500 BILLION"`, `"70 TAKES"`, `"16-HOUR DAYS"`, `"$40M"` |
| **`mono`** | `IBM Plex Mono`, `Space Mono` | 600 Monospace | Archival stamps, code variables, terminal outputs, dates, citations. | `"[BATCH S05]"`, `"reddit.py"`, `"VALUATION: $0"`, `"JUNE 2005"` |
| **`handwritten`** | `Caveat`, `Reenie Beanie` | 600–700 Cursive | Physical notes, taped polaroid captions, founder signatures, margin scribbles. | `"Steven Spielberg"`, `"Alexis Ohanian"`, `"notes from Paul"` |

### Caption Box Highlights (`w.box`)
- `'yellow'`: Fluorescent documentary evidence marker (`rgba(245, 197, 66, 0.95)` with `#0B0B0C` text). Used sparingly for the single core metric or revelation in a sentence.
- `'white'`: Crisp high-contrast box (`rgba(255, 255, 255, 0.95)` with `#0B0B0C` text) against dark footage.
- `'invert'`: Black box with white text for high-key stark slides.

---

## 4. The Optical Reset Rhythm ("The Contrast Flip")

The human eye quickly adapts to visual uniformity. If a reel stays dark for 10 seconds, viewers tune out.
**Rule of Pacing:**
1. **Never exceed 3.0 seconds on a single shot archetype.**
2. **Every 1.5 to 2.5 seconds, flip the optical luminance:**
   - Dark archival scene (Luminance < 20%)
   - $\rightarrow$ Stark White Slide or Document Crop (Luminance > 85%)
   - $\rightarrow$ Pinned Polaroid on neutral surface (Luminance ~ 50%)
   - $\rightarrow$ Dark terminal/IDE or high-contrast footage (Luminance < 25%)
3. This creates a physiological "reset" in the brain, dramatically extending watch time and completion rate.

---

## 5. Master Shot Archetypes Catalog

The Remotion engine (`DocReel.tsx`) implements these standard archetypes:

### Archetype 1: `video_cinematic`
- Full-bleed or letterboxed authentic video asset.
- Subtle, continuous forward zoom (`scale: 1.0 -> 1.06`).
- Subtle film grain and letterbox bars (`h_bar: 54px`).
- Dark vignette to protect caption legibility.

### Archetype 2: `stark_slide` (Optical Reset)
- Pure `#FFFFFF` (or deep `#060607`) full-bleed graphic slide.
- Three tiers of typography:
  - Top eyebrow: Monospace uppercase with tracking (`letterSpacing: 6px`).
  - Center punch: Massive condensed sans or serif italic quote.
  - Bottom citation: Subdued secondary caption (`#666666`).
- Fast camera punch/whip-zoom (`scale: 1.04 -> 1.0`).

### Archetype 3: `polaroid_card` (Physical Evidence)
- White photographic paper card (`padding: 16px 16px 44px 16px`) with physical drop shadow.
- Realistic semi-transparent drafting/masking tape pinned across the top edge (`transform: rotate(-3deg)`).
- Handwritten cursive label scribbled across the bottom margin or floating immediately above.
- Slight physical tilt (`rotate: -2deg` to `+3deg`).

### Archetype 4: `flanking_media`
- Centered 16:9 video frame floating against a high-contrast background.
- Captions split physically across the margins: left phrase on the left flank, right phrase on the right flank.
- Keeps the visual center clean while forcing the eye to scan horizontally.

### Archetype 5: `document_highlighter`
- High-resolution scan or render of an authentic document (Y Combinator acceptance email, Hacker News post, SEC filing, IMDb budget sheet).
- A kinetic highlighter box sweeps left-to-right across the key sentence or dollar figure.
- Synced to an audible marker squeak / highlight SFX.

### Archetype 6: `logo_constellation`
- Central bold thesis typography.
- Surrounding floating badges/icons of relevant software tools, logos, or companies with subtle floating physics (`spring({ damping: 12 })`).

---

## 6. Audio Engineering & Loudness Formulas

A video with incredible visuals but weak, muddy audio will fail immediately. Follow these exact audio formulas:

### A. Loudness Standards
- **Voiceover Peak:** `-0.5 dB to -0.1 dB True Peak`.
- **Integrated Voiceover Loudness:** `-14.0 dB to -16.0 dB mean / LUFS`.
- **Music Bed Level:** `-24.0 dB to -28.0 dB` (must sit 10–12 dB below narration at all times).
- **SFX Bursts:** `-12.0 dB to -18.0 dB` with fast decay.

### B. FFmpeg Voiceover Mastering Filter Chain
```bash
# Normalize and master voiceover to broadcast-loud standard:
ffmpeg -y -i raw_tts.mp3 -af "volume=1.45,alimiter=limit=0.98:attack=2:release=50" -ar 44100 -ac 2 voice_mastered.wav
```

### C. Multi-Track SFX & Music Bed Mixing Command
**CRITICAL:** Never use default `amix=inputs=3` without `:normalize=0`! Default ffmpeg `amix` divides every input stream by `1/N` (e.g. 1/3 = -9.5 dB cut), instantly destroying your voice volume!
```bash
ffmpeg -y \
  -i visual_silent.mp4 \
  -i voice_mastered.wav \
  -i sfx_track.wav \
  -i music_bed.mp3 \
  -filter_complex "[1:a]volume=1.35[v]; [2:a]volume=0.85[s]; [3:a]volume=0.18[m]; [v][s][m]amix=inputs=3:duration=first:normalize=0,alimiter=limit=0.98[outa]" \
  -map 0:v -map "[outa]" \
  -c:v copy -c:a aac -b:a 256k \
  -shortest master_final.mp4
```

---

## 7. Remotion Engine Pipeline Architecture

The engine lives at `D:\agency content\BIN\documentary_tofu\engine\`:
```
BIN/documentary_tofu/
├── engine/
│   ├── src/
│   │   ├── Root.tsx          # Composition entrypoint
│   │   ├── DocReel.tsx       # Master renderer (Shots, Captions, Effects, Google Fonts)
│   │   ├── theme.ts          # Color tokens, typography families, easings
│   │   └── types.ts          # TypeScript interfaces for EDL, Shots, Words
│   ├── editorial_edl.py      # Automated NLP tagging engine (words -> fontKind, box)
│   ├── render.mjs            # Headless Chrome runner (renders stills and mp4)
│   └── package.json
└── ep-D4-500b-living-room/   # Episode folder
    ├── build/                # Render assets & EDL
    │   ├── edl.json          # Compiled EDL with multi-font shots
    │   └── public/clips/     # Video, image, and card assets
    ├── build_edl.py          # Episode assembly script
    ├── sfx_mixer.py          # Sound design & audio muxing
    └── master_episode_d4.mp4 # Final delivery master
```

### Automated Multi-Font EDL Tagging Rules (`editorial_edl.py`)
1. **Numbers, Currency, Metrics** (`\$?\d+[\d,\.]*[MK%]?`): Tag as `fontKind: "condensed"` or `"mono"` with `box: "yellow"`.
2. **Emotional / Power Vocabulary** (`obsession`, `brutal`, `billion`, `genius`, `legendary`, `secret`, `dead`, `radical`): Tag as `fontKind: "serif-italic"`.
3. **Entity Names / Tech Companies** (`Reddit`, `Y Combinator`, `OpenAI`, `Nvidia`, `Steve`, `Alexis`): Tag as `fontKind: "mono"` or handwritten tag.
4. **Standard words**: Tag as `fontKind: "sans"`.

---

## 8. Quality Control Pre-Flight Checklist

Before presenting any finished video or marking an episode complete, verify:
- [ ] **Loudness Test:** Run `ffprobe -af "volumedetect"` on master audio; ensure `mean_volume` is between `-14.0 dB` and `-16.5 dB`.
- [ ] **Caption Contrast:** Ensure captions on pure white stark slides render with black text (`#0A0A0A` or dark pill), never white-on-white.
- [ ] **Spelling & Names:** Verify all proper nouns, founder names (e.g., *Steve Huffman*, *Alexis Ohanian*, *Paul Graham*), and dates are 100% accurate.
- [ ] **Asset Authenticity:** Zero hallucinated or generic UI frames. Use real historical screenshots, authentic founder photos, or real platform archives.
- [ ] **Rhythm Audit:** Check that an optical reset (stark slide or document crop) occurs at least once every 10 seconds.
- [ ] **Contact Sheet Proof:** Render and visually inspect a contact sheet of key frames before finalizing the delivery.

