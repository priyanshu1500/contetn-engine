# Content Engine for Foundery & LexIntent

> An autonomous, high-status content production and editorial system trained for **Foundery** (B2B AI Automation Agency) and **LexIntent** (Legal Tech / Student Platform). Built to consistently produce documentary reels and marketing assets that match or exceed top-tier editorial media like `@metromedia.house` and `@stanlaunchpad`.

---

## 📚 Essential Guidebooks & Knowledge Base

Before producing any creative assets or modifying the video rendering engine, read the following guidebooks:

1. **[`guidebooks/SKILLS_AND_TOOLING.md`](./guidebooks/SKILLS_AND_TOOLING.md)**: **MUST READ FOR NEXT AGENT.** Complete breakdown of all specialized AI skills (`emilkowalski/skills`, `pbakaus/impeccable`, `Leonxlnx/taste-skill`, `Agent-Reach`, `jakubkrehel/skills`, `ui-ux-pro-max`, `mattpocock/skills`), their official GitHub repos, one-command install commands, and how to operate them within this engine.
2. **[`guidebooks/REPLICATION_GUIDE_NEW_PC.md`](./guidebooks/REPLICATION_GUIDE_NEW_PC.md)**: Step-by-step setup on a fresh machine (Python, Node/Remotion, FFmpeg, Chrome Headless Shell, and audio mastering commands).
3. **[`guidebooks/THOUGHT_PROCESS_AND_RESEARCH.md`](./guidebooks/THOUGHT_PROCESS_AND_RESEARCH.md)**: Evolution history from generic AI slop to high-status documentary aesthetics, breakdown of user feedback loops, and forensic analysis of reference accounts.
4. **[`guidebooks/METROMEDIA_EDITORIAL_PLAYBOOK.md`](./guidebooks/METROMEDIA_EDITORIAL_PLAYBOOK.md)**: Frame-by-frame breakdown of MetroMedia pacing, shot archetypes, and multi-font kinetic captions.
5. **[`guidebooks/DESIGN_PHILOSOPHY.md`](./guidebooks/DESIGN_PHILOSOPHY.md)**: Core agency aesthetic standards, David Fincher camera creep rules, optical contrast resets, and strict bans.
6. **[`guidebooks/QC_CHECKLIST.md`](./guidebooks/QC_CHECKLIST.md)**: Pre-flight and post-render verification rubric (audio loudness, founder spelling, and typography checks).
7. **[`AGENTS.md`](./AGENTS.md)**: Autonomous agent operating protocol, non-negotiable taste mandates, and banned practices.
8. **[`VENTURES.md`](./VENTURES.md)**: Clear boundary separation between Foundery (B2B AI agency) and LexIntent (student resume & legal platform).

---

## 📁 Repository Structure

```
contetn-engine/
├── guidebooks/                             # Production SOPs, research, and skills guide
│   ├── SKILLS_AND_TOOLING.md               # Directory of agent skills, GitHub links & protocols
│   ├── REPLICATION_GUIDE_NEW_PC.md         # Setup instructions for a new machine
│   ├── THOUGHT_PROCESS_AND_RESEARCH.md     # Taste evolution and forensic reference breakdowns
│   ├── METROMEDIA_EDITORIAL_PLAYBOOK.md    # Frame-by-frame pacing & typography rules
│   ├── DESIGN_PHILOSOPHY.md                # Agency aesthetic standards & strict anti-slop rules
│   ├── PIPELINE.md                         # Technical render & mastering architecture
│   ├── QC_CHECKLIST.md                     # Step-by-step QC checklist
│   └── SCRIPT_FORMULA.md                   # 8-beat documentary persuasion script template
├── references/                             # Visual evidence and reference breakdowns
│   ├── metromedia_montage.jpg              # 20-frame visual breakdown of @metromedia.house
│   ├── stanlaunchpad_montage.jpg           # 20-frame visual breakdown of @stanlaunchpad
│   ├── metromedia_editorial_contact_sheet.jpg # Flagship Ep-D4 12-frame contact sheet
│   └── reference_analysis.md               # Rhythm, typography, and optical reset study
├── foundery/                               # Foundery B2B Content Engine
│   ├── engine/                             # Remotion v3 Engine (DocReel.tsx, StarkSlide, PolaroidCard)
│   ├── episodes/
│   │   ├── ep-D4-500b-living-room/         # Flagship Reddit documentary (all real clips, cards, EDL)
│   │   ├── ep-D3-one-person-unicorn/       # Sam Altman / AI leverage documentary reel
│   │   └── ep-C1-zappos/                   # Zappos origin documentary reel
│   ├── demos/                              # Node mascot reels (ep-001, ep-002, ep-003, _template)
│   └── strategy/                           # Brand guide, curiosity ladder, and funnel plans
├── lexintent/                              # LexIntent Student & Legal Tech Content System
│   ├── dossiers/                           # Format codex, asset sources, case files
│   ├── scripts_and_plans/                  # Script engine, reel system plan, upgrade notes
│   ├── templates/                          # Interactive HTML case-file renderers
│   └── voice/                              # Edge TTS voice pickers & testing harnesses
├── assets/
│   ├── fonts/                              # Typography tokens (Gambetta, Inter, Bebas, Caveat)
│   ├── sfx/                                # Tactile audio (whoosh, heavy shutter, impact)
│   ├── music/                              # Ambient documentary soundtrack beds
│   └── .env.example                        # Safe credentials template (zero API keys exposed)
├── AGENTS.md                               # Operational protocol, taste mandate & strict bans
├── SYSTEM_KNOWLEDGE_BASE.md                # Comprehensive architectural and creative guide
└── VENTURES.md                             # Clear venture boundary (Foundery vs. LexIntent)
```

---

## ⚡ Quick Replication on Any Machine

```bash
# 1. Clone repository
git clone https://github.com/priyanshu1500/contetn-engine.git
cd contetn-engine

# 2. Install Engine Dependencies
cd foundery/engine
npm install

# 3. Render Flagship Episode D4
cd ../episodes/ep-D4-500b-living-room
node ../../engine/render.mjs video
python sfx_mixer.py

# 4. Verify Master Audio Volume
ffmpeg -i master_episode_d4.mp4 -af "volumedetect" -vn -sn -dn -f null NUL
# Confirms mean volume between -14.0 dB and -16.5 dB
```