# Google Flow Automation — Second Asset-Generation Tool (alongside Gemini)

Google Flow (`flow.google.com`) is a **separate web app** from the Gemini
chat interface documented in `GEMINI_ASSET_AUTOMATION.md` — same Google
account, same underlying image models in places, but a genuinely different
UI built for structured, multi-shot production rather than a single chat
thread. Required alongside Gemini for every episode from ep-002 onward
(standing instruction from the user, 2026-09-15) specifically because it
covers two things Gemini's chat interface doesn't do well: keeping a
recurring visual element consistent across multiple separate shots, and
generating more than one frame/variation per prompt in a single pass.

Access: same browser-automation pattern as Gemini — `opencli browser
<profile> open "https://flow.google.com/"`, same logged-in-Chrome
assumption, same profile (`ygnt53g4` confirmed working). Account shown
logged in with a `PRO` badge — Flow-specific paid tier, separate from
whatever plan the Gemini side is on.

## 1. What Flow has that Gemini's chat doesn't

- **Characters panel** — define a recurring character/prop once, reuse it
  consistently across many separate generations instead of re-describing it
  in every prompt and hoping the composition matches. Directly useful for
  anything episode-specific that needs to recur across multiple *separate*
  shots (not the mascot bookends, which already have their own proven
  same-thread "animate this image" technique in Gemini — use Flow's
  Characters for something else that needs to persist across more than two
  shots, e.g. a consistent desk/prop set reused across several cutaways).
- **Scenes panel** — same idea, for a location/setting rather than a
  character.
- **Batch generation, x1/x2/x3/x4** — generate up to 4 variations of one
  prompt in a single pass (in the per-project "Agent settings" panel, under
  "Image generation default"). Use this to get more frame options per shot
  instead of settling for the first single generation — directly answers
  the standing instruction to "add more than 2-3 frames of generated
  [assets] per reel."
- **Native aspect-ratio picker**: 16:9 / 4:3 / 1:1 / 3:4 / **9:16** — pick
  9:16 for every Reels/Shorts asset, same as Gemini's `--ar 9:16` prompt
  suffix achieves there.
- **Image models available** (as of this writing, in the model dropdown):
  Nano Banana Pro, Nano Banana 2, Nano Banana 2 Lite.

## 2. Basic workflow

1. Open or create a project: `https://flow.google.com/project/<id>` (an
   existing project's id, from the homepage grid) or use "New project" from
   the homepage if starting clean.
2. The main prompt box ("What do you want to create?") sits at the bottom
   of the project view — type the prompt, use the "+" to attach a
   reference image if building on an existing Character/Scene, the sliders
   icon for per-generation settings, and the arrow to submit.
3. **"Confirm before generating" defaults to Always** (in Agent settings) —
   Flow will ask for confirmation before spending credits on each
   generation. This is a real per-account credit system
   ("Learn about generation costs" links to it) — don't set this to
   "Never" (auto-spend) without the user's explicit say-so.
4. Generated assets land in the project's "All media" grid — download from
   there the same way you'd download from a Gemini chat thread (inspect the
   page for a download control; exact selector wasn't fully mapped this
   session — verify via `opencli browser <profile> find --css "button"` and
   look for a download/export aria-label before assuming one exists).

## 3. Flakiness — identical pattern to Gemini, same fix applies

Flow hit the *exact same* `about:blank` reset-loop symptom as Gemini's chat
interface in the same session — this is very likely a shared root cause
(the underlying Chrome/CDP browser-automation layer, not something specific
to either Google product). When it happens:
1. Check state: `opencli browser <profile> state` — look for `url:
   about:blank`.
2. Reopen fresh: `opencli browser <profile> open "https://flow.google.com/"`
   (or the specific project URL).
3. If it recurs identically on a retry, and **also** reproduces on a
   completely unrelated site in the same browser profile (as happened this
   session — Gemini and Flow both broke back-to-back), stop retrying
   automated fixes and tell the user directly: this points to the browser
   session itself, not either website, and needs a manual check (an
   unresponsive tab, a stuck permission dialog, or Chrome itself needing a
   restart) that automation can't see or fix.

## 4. What's still unverified — check before relying on it

This section was written from a single exploration session, not repeated
production use. Before treating the following as settled fact, verify
directly:
- **Video generation model and workflow** — only the image-generation
  settings panel (Nano Banana Pro/2/2 Lite) was actually opened this
  session. Flow is explicitly billed as a video tool too (a Veo-family
  model is likely reachable from the same project view) but its specific
  workflow, output format, and download pattern were not exercised.
- **The exact download-button selector(s)** for images/videos in a
  project's media grid.
- **Whether Characters/Scenes assets can be pulled into Gemini's same-
  thread "animate this image" technique**, or whether Flow's own animation
  path should be used end-to-end instead once a still is approved there.

If you hit any of these, resolve it once and fold the concrete answer back
into this doc — don't leave the next agent to rediscover it.
