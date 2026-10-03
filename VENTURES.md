# Ventures overview — read this first, don't conflate these

Written 2026-09-23 after a correction from the user: earlier sessions in this workspace mixed
up which brand a piece of content belongs to. This file is the standing reference so that
doesn't happen again. Two **separate ventures**, separate audiences, separate funnels,
separate CTAs. Verified against the actual files in each folder where noted; anything not
yet documented in-repo is marked as **(stated by user, 2026-09-23)**.

---

## 1. LexIntent — the platform (student-facing)

**What it is:** a platform for students (law students specifically, India-focused per the
existing research) built around a **resume analyser** product. **(confirmed in-repo:**
`lexintent/dossier-01.html`, `lexintent/reel-system-plan.html`, `lexintent/script-engine.html`,
`lexintent/format-codex.html` — a real, researched Instagram growth strategy already exists.)*

**The funnel, per the user (2026-09-23):** Instagram content → **a quiz** that onboards
students as users of the platform → **the resume analyser** as the paid/core product.
The quiz is the mid-funnel onboarding mechanic; it is not yet documented in the `lexintent/`
files as of this writing — build/spec it as a new artifact when it's time (a MOFU-style
handoff, similar in spirit to `ai-agency/FUNNEL_CONTENT_PLAN_v1.md`, but LexIntent's own).

**Content engine (confirmed in-repo):**
- Editorial/documentary-style Instagram reels — "Case File," "dossier," "two resumes"
  comparison formats. Real files: `lexintent/reel-case-file-001.html`,
  `reels/case-file-001`, `reels/case-file-002`, `reels/two-resumes-v2`,
  `lexintent/_refs/mzm-two-resumes*.mp4`.
- A researched **hook/script formula** reverse-engineered from a real, successful Indian
  Instagram page (a labour-law consultancy, ~61k followers) and re-pointed at law students:
  hook (threat/command, second-person, high stakes) → turn (the reframe — "you have power
  here") → payload (the exact fix, numbered) → proof (before/after) → CTA (comment a keyword
  → DM). See `lexintent/reel-system-plan.html` for the full formula and a 10-hook starter
  bank aimed at CV/placement fears (e.g. weak resume lines, non-NLU discrimination, vague
  phrases like "assisted with research").
- A competitive dossier of real Instagram accounts in the law-career niche (`@traceyourcase`,
  `@lawctopus.official`, `@legalshotswithvakeel`, etc.), with the finding that **"comment
  [keyword] → I DM you a resource"** is the working growth mechanic in this exact niche right
  now, and that lean/high-production beats high-volume/generic (a 291-post account
  out-engaging a 3,509-post account).
- An illustration pipeline plan (DiceBear/Humaaans/Open Peeps/unDraw, all free/CC0-or-MIT,
  recolored to LexIntent's oxblood/kraft palette) and an Indian-voice pipeline plan (Sarvam AI
  Bulbul v3 recommended first choice, ElevenLabs as fallback, Hinglish captions where the
  topic suits).
- Visual register: an editorial/documentary "dossier" look (oxblood/paper/Newsreader-serif
  aesthetic) — **not** the same visual system as either the Foundery Node-mascot content or
  the `documentary_tofu` engine's v2 dark/mono palette (see below). Keep these visually
  distinct; they serve different brands.

**Open question, not yet resolved:** `projects/reel_bloodless_coup` (the Altman-vs-Musk
documentary reel built earlier this session) shares the same `assets/` library, whose own
README calls itself the "LexIntent asset library." It is **not confirmed** whether
Bloodless Coup was meant to publish under the LexIntent brand or was a topic/engine
experiment that happened to reuse shared infrastructure — its subject (AI industry power
struggles) doesn't match LexIntent's actual audience (law students / career anxiety) or its
Instagram-native short-reel format (Bloodless Coup runs ~95s with a very different visual
grammar). **Ask before assuming either way** if this comes up again.

---

## 2. Foundery — the AI automation agency (business-owner-facing)

**What it is:** a completely separate venture — a page/brand for the AI automation agency.
Everything built so far under the `ai-agency/` folder belongs here: the Node mascot, the
warm-paper/blue-orange brand system (`ai-agency/brand.md`), the TOFU/MOFU/BOFU funnel scripts
(`ai-agency/FUNNEL_CONTENT_PLAN_v1.md` — T1/T2/M1/M2/B1/B2, plus the LexIntent-resume-analyser
demo script written 2026-09-23 which is *itself* a Foundery-style MOFU proof-of-work script
**about** LexIntent's product — that's a Foundery episode with LexIntent as its subject
matter, not a LexIntent-brand asset), the documentary-TOFU episodes under
`ai-agency/documentary_tofu/` (the Klarna case study, the reusable DocReel engine, its v2
dark/mono visual language), and the Curiosity Ladder scriptwriting rule
(`ai-agency/CURIOSITY_LADDER.md`).

**Audience:** business owners/operators paying for manual labor they'd rather replace with a
system (real estate, marketing agencies, hotels, recruiting — per `brand.md`), not students.

**Funnel:** documentary-TOFU and Node-mascot content → comment-to-DM or "book a call" →
a systems-sales conversation. See `ai-agency/FUNNEL_CONTENT_PLAN_v1.md` for the full breakdown.

**Note on the earlier "LexIntent, the resume analyser" script (2026-09-23):** that script was
written using the Foundery production format (Node poses, header pills, progress bar) as a
MOFU-style proof-of-work demo, with LexIntent's resume analyser as the featured automation.
**Whether that script should actually run on the Foundery page (as a "look what AI can build"
case study) or be rewritten in LexIntent's own dossier/case-file visual language (to run on
LexIntent's own account) is an open decision — ask before producing final assets.**

---

## Rule going forward
Before writing a script, building an EDL, or picking a visual system: confirm **which
venture** the work is for. LexIntent = students, resume analyser, dossier/case-file
documentary aesthetic, comment-to-DM → quiz → product. Foundery = business owners,
automation systems, Node mascot or the DocReel dark/mono documentary engine, comment-to-DM →
book a call. Don't default to whichever one was worked on most recently in the conversation.
