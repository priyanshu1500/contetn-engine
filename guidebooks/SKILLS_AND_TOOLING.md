# SKILLS_AND_TOOLING.md: Agent Skills, Repositories & Execution Protocols

> **Target Audience:** Any autonomous AI agent, pair-programmer, or human engineer operating in this repository.  
> **Purpose:** Document all specialized agent skills and CLI tools that power the research, editorial taste, motion design, and QA of this content engine—including official GitHub sources, one-command installation, and concrete operational protocols.

---

## 1. Why These Skills Are Required

Default AI coding assistants tend to produce **generic AI slop**:
- Repetitive, predictable UI templates (e.g. standard fake ChatGPT windows or generic terminal frames).
- Monotonous, floaty motion curves without physics, snap, or intention.
- Flat typography with single-font bottom subtitles and karaoke highlights.
- Inaudible voiceovers drowned out by background audio.

The skills documented below provide the **durable taste layer, motion physics, and research intelligence** that allow autonomous agents in this repository to consistently output broadcast-level, high-status content matching accounts like `@metromedia.house` and `@stanlaunchpad`.

---

## 2. Complete Skills Directory & Official GitHub Repositories

### A. Research & Social Media Intelligence
Used to scrape, inspect, and analyze high-performing reference reels and real-world archival footage.

| Skill / Tool | Description | Official GitHub Repository |
|---|---|---|
| **`agent-reach`** | Universal social & web research engine across 16 platforms (Instagram Reels, YouTube, Reddit, X/Twitter, Bilibili, etc.). Used to pull reference videos and parse pacing/captions. | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) |
| **`opencli`** | High-performance CLI backend for querying social media APIs and public pages without browser overhead. | [jackwener/opencli](https://github.com/jackwener/opencli) |

### B. Anti-Slop, Editorial Aesthetics & Visual Taste
Used to enforce the agency design grammar, stark optical resets, and high-contrast typography.

| Skill Suite | Included Skills | Focus & Responsibilities | Official GitHub Repository |
|---|---|---|---|
| **`Leonxlnx/taste-skill`** | `taste-skill`, `soft-skill`, `minimalist-skill`, `redesign-skill`, `brandkit` | Anti-slop frontend and visual grammar. Prevents generic templates, enforces warm monochrome palettes, editorial bento grids, and high-status brand kits. | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |
| **`pbakaus/impeccable`** | `impeccable` (audit, polish, adapt, critique) | Enforces design system constraints, scores visual craft, and eliminates AI design cliches (e.g., purple gradients, identical cards). | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| **`nextlevelbuilder/ui-ux-pro-max-skill`** | `ui-ux-pro-max` | Massive searchable design knowledge base (79 UI styles, 192 product palettes, 74 font pairings, 119 UX guidelines). | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| **`bencium-design-skill`** | `bencium-innovative-ux-designer`, `bencium-controlled-ux-designer` | Independent visual systems, expressive negative space, and accessible UI protocols. | [bencium/bencium-claude-code-design-skill](https://github.com/bencium/bencium-claude-code-design-skill) |

### C. Motion Physics, Timing & Easing
Used inside Remotion compositions (`DocReel.tsx`) for kinetic text scaling, camera creeps, and card slides.

| Skill Suite | Included Skills | Focus & Responsibilities | Official GitHub Repository |
|---|---|---|---|
| **`emilkowalski/skills`** | `emil-design-eng`, `animate`, `review-animations`, `apple-design`, `animation-vocabulary`, `find-animation-opportunities` | Motion engineering principles by Emil Kowalski (Linear, Vercel). Physics-based spring animations, exponential ease-outs, entrance punches, and gesture physics. | [emilkowalski/skills](https://github.com/emilkowalski/skills) |

### D. Typography, Color Systems & Micro-Polish
Used for rendering bespoke cards (e.g. 2005 Reddit UI, Paul Graham quote cards) with authentic print and screen aesthetics.

| Skill Suite | Included Skills | Focus & Responsibilities | Official GitHub Repository |
|---|---|---|---|
| **`jakubkrehel/skills`** | `better-ui`, `better-typography`, `better-colors`, `better-layout`, `better-accessibility`, `better-icons` | Exact typographic scales, tracking, leading, optical alignment, and contrast-ratio verification. | [jakubkrehel/skills](https://github.com/jakubkrehel/skills) |

### E. Agent Protocols, Script Stress-Testing & Code Review
Used to validate documentary scripts, debate thesis angles, and maintain modular architecture.

| Skill Suite | Included Skills | Focus & Responsibilities | Official GitHub Repository |
|---|---|---|---|
| **`mattpocock/skills`** | `research`, `code-review`, `codebase-design`, `diagnosing-bugs`, `domain-modeling`, `grilling`, `tdd`, `to-spec`, `writing-for-agents` | Relentless stress-testing of controversial script claims (`grilling`), deep module separation, and structured agent documentation. | [mattpocock/skills](https://github.com/mattpocock/skills) |

---

## 3. Installation Guide for a Fresh Machine / Agent

### Option 1: Standard Universal CLI (`npx skills`)
Most modern AI agent platforms (Antigravity, Claude Code, Cursor, Windsurf) support the universal skills runner:

```bash
# 1. Install Global CLI Tooling
npm install -g @jackwener/opencli

# 2. Add Research & Social Scraping
npx skills add https://github.com/Panniantong/Agent-Reach

# 3. Add Motion & UI Engineering
npx skills add emilkowalski/skills
npx skills add jakubkrehel/skills
npx skills add pbakaus/impeccable

# 4. Add Taste & Anti-Slop Intelligence
npx skills add https://github.com/Leonxlnx/taste-skill
npx skills add nextlevelbuilder/ui-ux-pro-max-skill
npx skills add https://github.com/bencium/bencium-claude-code-design-skill

# 5. Add Agent Protocol & Stress-Testing
npx skills add mattpocock/skills
```

### Option 2: Direct Directory Clone (Offline / Air-Gapped)
If `npx skills` is not supported, clone or copy the repository folders directly into your agent's skills configuration directory:
- **Antigravity / Gemini CLI:** `C:\Users\<USER>\.gemini\config\skills\` (or `~/.gemini/config/skills/`)
- **Claude Code:** `~/.claude/skills/`
- **Cursor / VS Code:** `.cursor/rules/` or project root `.skills/`

```bash
cd ~/.gemini/config/skills/
git clone https://github.com/Panniantong/Agent-Reach.git agent-reach
git clone https://github.com/emilkowalski/skills.git emil-skills
git clone https://github.com/pbakaus/impeccable.git impeccable
git clone https://github.com/Leonxlnx/taste-skill.git taste-skill
git clone https://github.com/jakubkrehel/skills.git jakub-skills
git clone https://github.com/nextlevelbuilder/ui-ux-pro-max-skill.git ui-ux-pro-max
git clone https://github.com/mattpocock/skills.git mattpocock-skills
```

---

## 4. How the Next Agent Must Use These Skills in This System

When executing tasks in this repository, follow this workflow:

### Step 1: Script Drafting & Concept Stress-Testing
* **Trigger:** Writing or revising `narration.txt` for an episode.
* **Skill to Invoke:** `grilling` (from `mattpocock/skills`).
* **Protocol:**
  - Before rendering, stress-test controversial claims or thesis hooks.
  - Ban generic startup tropes ("Most people think X, but actually Y"). Focus on authentic documentary drama (e.g. Alexis and Steve's 2005 train ride, the Conde Nast fire-sale, the ghost profiles).
  - Verify founder names, dates, metrics, and quotes with `research`.

### Step 2: Reference Deconstruction & Pacing Benchmarking
* **Trigger:** Auditing why a reel is lacking watch time or virality compared to `@metromedia.house`.
* **Skill to Invoke:** `agent-reach` + `opencli`.
* **Protocol:**
  - Ingest reference Instagram URLs using `agent-reach` to examine frame rate, cut cadence, and visual transitions.
  - Generate visual contact sheets using FFmpeg (`ffmpeg -i ref.mp4 -vf "select='not(mod(n\,15))',scale=270:480,tile=5x4" -frames:v 1 contact_sheet.jpg`).
  - Study font-switching and word-by-word visual rhythm against `guidebooks/METROMEDIA_EDITORIAL_PLAYBOOK.md`.

### Step 3: Bespoke Card Creation (Anti-Slop Mandate)
* **Trigger:** Generating supporting graphics, UI cards, or archival newspaper clippings.
* **Skills to Invoke:** `taste-skill`, `better-typography`, `better-colors`.
* **Protocol:**
  - **NEVER** generate a generic ChatGPT prompt box or fake terminal UI. The user explicitly flagged this:
    > *"the assets like the chatgpt window frame etc are getting repeated in every other video that just makes our page look more predictable and fake fix that"*
  - Use Python Pillow (`make_reddit_cards.py`, `make_pg_card.py`) to generate bespoke historical UI:
    - 2005 Wayback Machine Reddit layout with classic blue links `#0000FF` and authentic Reddit alien logo.
    - Paul Graham Hacker News quote card on parchment paper texture `#F6F6EF`.
    - Photoreal polaroid paper cards with semi-transparent masking tape and handwritten name tags (`Caveat` font).

### Step 4: Motion Implementation in Remotion
* **Trigger:** Editing `DocReel.tsx` or building transitions in `engine/`.
* **Skill to Invoke:** `emil-design-eng` + `animate`.
* **Protocol:**
  - Use exponential ease-out curves (`interpolate(frame, [start, end], [0.92, 1.0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' })`).
  - Cap camera scale creep between `1.0` and `1.04` across 2.0–3.0 seconds (subtle David Fincher forward push, never disorienting fast zooms).
  - Multi-font caption switching (`WordCap`): dynamic font family assignment (`Bebas Neue` for numbers, `Playfair Display Italic` for power adjectives, `IBM Plex Mono` for code/data, `Inter` for speech).

### Step 5: Audio Verification (Strict Loudness Mandate)
* **Trigger:** Running `sfx_mixer.py` or mastering final output.
* **Skill to Invoke:** `QC_CHECKLIST.md` + FFmpeg `volumedetect`.
* **Protocol:**
  - Master VO volume: must **never** fall below `-16.0 dB mean volume`.
  - Always use `amix=inputs=3:duration=first:normalize=0` with `alimiter`.
  - Verify every master:
    ```bash
    ffmpeg -i master.mp4 -af "volumedetect" -vn -sn -dn -f null NUL
    ```
    Ensure `mean_volume` is between `-14.0 dB` and `-16.5 dB`.

---

## 5. Summary Cheat Sheet for Agents

```
Task                              Recommended Skill               Command / Action
-------------------------------------------------------------------------------------------------------------
Stress-test controversial hook    grilling                        Run thesis interview against SCRIPT_FORMULA.md
Ingest reference Instagram video  agent-reach / opencli           agent-reach analyze <url>
Design authentic UI card          taste-skill / better-typography Custom Pillow script with authentic typography
Tune Remotion easing & physics    emil-design-eng / animate       DocReel.tsx spring/interpolate settings
Verify pre-flight quality         QC_CHECKLIST.md                 Contact sheet generation & volumedetect
```
