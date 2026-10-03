# Gemini Web Automation — Photoreal Hero Shot Generation

How we generate the photoreal "hero" cinemagraph shots (mascot bookends at
the hook/CTA) using the Gemini **web app** (not the paid API) via browser
automation. Written for reuse by any AI assistant with `opencli` access.

Why the web app and not the API: the account already has a Gemini
Pro/Advanced subscription; the user does not want to pay for a separate API
key. `opencli` drives the user's real, already-logged-in Chrome directly —
two profiles are kept open: `ygnt53g4` (default/images) and `whghbej8`
(video).

---

## 1. Guaranteeing a truly fresh chat (read this before anything else)

**Root cause, found the hard way:** navigating to `https://gemini.google.com/app`
does **not** reliably start a blank conversation — it's client-side-routed
and can silently resume whatever conversation was last active in that
browser profile. This is not a rare edge case: it happened identically on
two separate "fresh" runs in the same session, both times returning the
exact same byte-identical unrelated image (a 12-slide pitch deck from a
completely different past task) instead of generating anything new. The
`wait_for("img.image.animate.loaded", ...)` check in `gemini_animate.py`
passed immediately both times, because that stale image was already loaded
on the page — there was nothing wrong with the click or the send, the
script was just looking at the wrong conversation entirely.

**The fix:** explicitly click the "New chat" control after opening the app
URL, don't rely on the URL alone:
```bash
opencli browser <profile> open "https://gemini.google.com/app"
opencli browser <profile> click "a[aria-label='New chat']"
```
This is now baked into `gemini_animate.py` itself (see its `main()`) — if
you're calling it as a script you get this for free. If you're driving the
browser by hand or with a different tool, don't skip this step just because
the URL "looks like" it should be a fresh session.

**How to catch it if it still slips through:** don't just check that an
image appeared — sanity-check that its *content* plausibly matches the
prompt before spending a video-generation step animating it. A one-line
gut check (does this look like what I asked for, even roughly?) would have
caught the pitch-deck mismatch immediately, before wasting the animate step
on it.

## 1b. Check for an existing usable generation before spending new credits

Before generating anything new, consider whether the account's chat history
already has a usable result — Gemini's web app keeps a `Recent` list in the
left sidebar and dedicated `Images`/`Videos` library tabs. If the user
mentions "the one generated at [a gemini.google.com/app/<id> URL]" or
similar, open that exact URL directly and pull the asset from there instead
of regenerating:
```bash
opencli browser <profile> open "https://gemini.google.com/app/<conversation-id>"
```
Then download directly from that thread (see §4 "Post-processing" for the
download-button pattern). This is strictly better than regenerating: zero
new credits spent, zero risk of a different take drifting from an
already-approved composition. Only regenerate when no existing asset
actually fits — don't default to a fresh generation out of habit.

## 2. The core technique: same-thread "animate this image"

Generating a video from a text prompt directly often produces a
composition you didn't approve and can't iterate on. The reliable pattern:

1. Generate a **still image** first, in a fresh chat.
2. In the **same chat thread**, immediately follow up: *"Animate this
   image: [motion instruction]."*
3. Gemini animates that exact approved composition — guaranteed matching
   subject/framing, because it's the same image, not a new generation.

This is implemented end-to-end in
`reels/_kit/microassets/gemini_animate.py`:
```bash
py -3 gemini_animate.py "<image prompt>" "<motion instruction>" <out.mp4> \
    --keep-still <out-still.png> [--profile ygnt53g4] [--ar 9:16]
```

## 3. The cinemagraph prompt pattern (the actual production-value trick)

Reverse-engineered from a reference asset literally named
`Image_to_video_Keep_all_backg.mp4`. The insight: don't animate the whole
scene — animate **one small, forgiving element** and explicitly lock
everything else. This plays to what video-gen models are actually good at
(ambient motion) and hides what they're bad at (holding sharp detail
stable).

**Image prompt template:**
```
Macro toy photography, shallow depth of field, warm cinematic desk
lighting. A small robot character called Node: matte dark charcoal
rounded-square body, one glowing soft blue dot eye, thin dark
capsule-shaped limbs, no other facial features, sitting on an open
notebook with cream/beige grid paper. Node holds/does [ACTION SPECIFIC TO
THIS EPISODE'S BEAT]. In the background, softly blurred bokeh: [1-2 desk
props]. Warm beige and blue color palette, photoreal render,
product-photography quality, 9:16 vertical composition, cinematic rim
light on Node's body.
```

**Motion/animate prompt template:**
```
Keep the entire background and composition exactly as-is, completely
locked and static — the notebook, the desk, [named background props] must
not move or warp at all. Only animate [ONE OR TWO SMALL THINGS]: e.g.
Node's eye gently pulsing brighter and dimmer, and a few soft glowing
light particles slowly drifting upward.
```

The explicit "keep background locked... must not move or warp at all" plus
naming exactly what's allowed to move is what makes this reliable. Never
ask for whole-scene animation.

## 4. Post-processing into a usable loop

```bash
ffmpeg -y -i "<downloaded>.mp4" -t <duration> -c:v libx264 -crf 18 \
    -pix_fmt yuv420p -an "<episode>/hero/<name>-hero.mp4"
```
- Trim to exactly the on-screen duration needed (e.g. 4.6s for a 4.3s cue +
  a little buffer for the fade-out).
- Strip audio (`-an`) — sound comes from the soundbed pipeline, not the
  Gemini clip.
- In `build.py`, composite via the `hero_bg()` helper, which scales/crops
  to fill 1080×1920 and fades out right at the cue boundary so the flat UI
  section picks up cleanly (see `PIPELINE.md` §2F).

## 5. Flakiness playbook (real, acknowledged, not a script bug)

The Gemini web UI has genuine day-to-day instability. Symptoms observed and
their fixes, in the order to try them:

1. **"Image never appeared" / prompt sits filled but unsent.** The Send
   button click didn't register (Angular timing). Retry the click 2-4
   times with ~2-3s between attempts:
   ```bash
   opencli browser <profile> click "button[aria-label='Send message']"
   ```
   If that still doesn't work, check whether the tab silently reset:
   ```bash
   opencli browser <profile> state   # look for url: about:blank
   ```
   If it did, reopen and retry fresh:
   ```bash
   opencli browser <profile> open "https://gemini.google.com/app"
   ```
2. **Still stuck after a fresh reload + retries.** Inspect the page text
   directly for a quota message before assuming it's a click bug:
   ```bash
   opencli browser <profile> eval "document.body.innerText.slice(-1500)"
   ```
   Look for *"I can create more images as soon as your limit reset. Check
   your usage in Settings"* — this is a real per-account rate limit, not
   fixable by retrying. Wait for it to reset (ask the user) or generate
   fewer images per session.
3. **A downloaded file doesn't match what you expect** (e.g. it turns out
   to be a stale reference image, not the new generation). Don't assume —
   verify by screenshotting the live chat (`opencli browser <profile>
   screenshot <path>`) and reading the image before trusting a download.
   Filenames from Gemini are unpredictable (derived from prompt text or
   generic `Gemini_Generated_Image_*.png`), so diff the download directory
   (`D:\DOWNLOADS`) before/after the action rather than globbing a fixed
   name.
4. **A single paused frame looks broken** (e.g. limbs scattered,
   incoherent). Don't conclude the whole generation failed from one frame
   — download the actual video and inspect multiple frames across its full
   duration; a mid-transition frame can look wrong while the settled
   result is fine. Use the `/watch` skill (see below) to check properly
   rather than eyeballing a single screenshot.
5. **After 3 full retry cycles with no progress**, stop and tell the user
   plainly rather than continuing to burn turns — recommend a manual
   browser refresh/retry, or ask them to send the prompt manually and hand
   off from wherever the browser lands.

## 6. Verifying a generated asset properly

Always use the `/watch` skill (bundled `claude-video` plugin) to inspect a
generated video before wiring it into `build.py` — a single screenshot can
catch a mid-transition frame and look broken when the settled clip is
fine, or vice versa:
```bash
python "<watch skill dir>/scripts/watch.py" "<video path>" --detail token-burner
```
Then Read every listed frame path before judging quality.

## 7. Related scripts

- `reels/_kit/microassets/gemini_fetch.py` — plain image generation, no
  animate follow-up.
- `reels/_kit/microassets/gemini_fetch_video.py` — text-to-video directly
  (use only when there's no still to lock composition to first).
- `reels/_kit/microassets/fetch_assets.py` — NOT Gemini; pulls generic
  icons (Iconify) and real logos (Logo.dev) via a headless browser
  screenshot + ffmpeg crop/recolor. Use for micro-assets, not hero shots.

All Gemini-generated assets get logged to
`assets/generated/manifest.json` (prompt, file path, timestamp, source) —
append to this, don't skip it, so a future session can find/reuse an asset
instead of regenerating it.
