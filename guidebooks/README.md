# ai-agency Docs — Start Here

This folder is the complete, self-contained handoff package for the
`ai-agency` reel production system. It exists so **any AI assistant** —
Claude, Gemini, an Antigravity agent, a GPT-based agent, whatever runs this
next — can pick up this project cold, with no prior conversation history,
and produce a new episode to the exact same standard, or review/fix an
existing one.

**On tool-agnosticism:** these docs were written inside a Claude Code
session and name its actual tools where precision matters (`opencli` for
browser automation, `ffmpeg`/`ffprobe` by path, Python scripts by path) —
that's intentional, not an oversight: a vague "use a browser automation
tool" is useless when the exact bug fixes (below) live in the exact
selectors and click sequences. If you are a different agent, the required
underlying capabilities are: (1) run arbitrary shell/Python commands, (2)
drive a real, already-logged-in Chrome browser — open a URL, screenshot it,
read its DOM/text, fill a field, click an element — and (3) read/write local
files and images. Map `opencli browser <profile> <verb>` calls to whatever
your equivalent tool's verbs are; the sequence of steps and the reasoning
behind each one carries over exactly even when the tool name doesn't. Do
not skip a step because your tool "probably" handles it differently —
verify against the actual failure modes documented here first.

## Read in this order

1. **`../brand.md`** — the locked brand spec: exact hex colors, typography
   rules, the mascot ("Node") design, CTA options. The source of truth for
   "what does this look like."
2. **`DESIGN_PHILOSOPHY.md`** — the *why*: the two-layer visual grammar,
   borrowed cinema-craft rules, the mascot system's two asset tiers, every
   real failure mode we hit and explicitly rejected. Read this before
   making any creative judgment call.
3. **`PIPELINE.md`** — the *how*: the exact, reproducible technical SOP,
   folder structure, every script and its exact invocation, the full
   `build.py` architecture, and a table of common bugs with fixes.
4. **`GEMINI_ASSET_AUTOMATION.md`** — how the photoreal mascot hero shots
   get generated via Gemini's web app (not the paid API), including the
   exact prompt templates and the flakiness playbook.
5. **`FLOW_ASSET_AUTOMATION.md`** — how to use Google Flow (a second,
   separate web tool from Gemini proper) for image/video generation,
   required alongside Gemini for every episode from ep-002 onward — its
   Characters/Scenes features and batch generation cover things Gemini's
   chat interface doesn't.
6. **`QC_CHECKLIST.md`** — run this, literally item by item, before calling
   any episode done.
7. **`SCRIPT_FORMULA.md`** — the required 8-beat persuasion structure for
   every buyer-facing script (hook → gap stat → moat insight → adoption-gap
   FOMO → capability listicle → punchline → stacked CTA → sign-off),
   reverse-engineered from a proven automation-sales creator. Write every
   new episode's VO against this before touching production.

## Reference episodes

`../demos/ep-001-inbox-to-crm/` is the first fully-delivered episode — its
`build.py`, `narration.json`, `sound-calm.json`, and `delivery/` folder are
a concrete reference implementation of the core system (mascot, hero
bookends, evidence cards, Proof Layer, sound). Read it for the baseline.

`../demos/ep-002-missed-call-agent/` supersedes it on script quality and
adds two techniques ep-001 didn't have: a dashboard-infographic evidence
card and a persistent pinned claim-strip (both described in `PIPELINE.md`
§2B and §2F respectively). Its `SCRIPT.md` is also a worked example of applying
`SCRIPT_FORMULA.md` end to end, including a documented rewrite history
(v1 → v2 → v3) showing *why* each revision was better, not just what
changed. If the two episodes' `build.py` ever disagree on a technique,
ep-002's is the newer, corrected version — check its dated comments.

## Reference material this system relies on

These were installed as Claude Code skills in the session that built this
system — if you're a different agent without a skill-loading mechanism,
treat the bullets below as **reading material to fetch and internalize
once**, not tools you invoke; the actual technique then lives in this
folder's docs, not in the skill itself:
- `video`, `image` — cinematography/art-direction reference (dramaturgy,
  camera rules, model-specific prompt syntax). Source: smixs/visual-skills.
- `01-viral-hook` through `10-podcast-visual` — Seedance 2.0 prompt-
  engineering patterns per content archetype. Source:
  rediumvex/ai-video-generator-claude.
- `watch` (claude-video plugin) — frame-by-frame video inspection: downloads
  a video, extracts scene-aware frames, transcribes audio. Used for QC and
  for verifying any newly generated Gemini/Flow asset before trusting it,
  and for reverse-engineering a competitor's script structure (see
  `SCRIPT_FORMULA.md`'s origin). If you lack an equivalent, the fallback is
  `yt-dlp` + `ffmpeg` frame extraction + any speech-to-text API — the
  technique matters more than the specific tool.

If working from a different machine/account (Claude Code or otherwise),
reinstall/re-source these first — the design philosophy and pipeline docs
assume the *knowledge* in them is available, however you get it.
