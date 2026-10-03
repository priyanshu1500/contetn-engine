# Pre-Delivery QC Checklist

Run every item below before copying a file into `delivery/` and calling an
episode done. Every item here traces back to a real bug caught in
production on this project — this is not a generic best-practices list.

## 1. Audio

- [ ] Run `silencedetect` on the raw VO **before** building: any gap should
      be ~0.3-1.0s. An outlier (2s+) is dead air, not a stylistic pause —
      trim it (see `PIPELINE.md` §2A) and re-derive all downstream timings.
      ```bash
      ffmpeg -i vo.mp3 -af "silencedetect=noise=-35dB:d=0.3" -f null - 2>&1 | grep -i silence
      ```
- [ ] Run `silencedetect` again on the **final muxed** file with a stricter
      threshold — the music bed/room-tone should fill everything, so there
      should be zero gaps ≥1s:
      ```bash
      ffmpeg -i <final>.mp4 -af "silencedetect=noise=-40dB:d=1.0" -f null - 2>&1 | grep -i silence
      ```
- [ ] Listen for (or spot-check the spectrogram around) any spliced edit
      point — cut points should sit well inside a confirmed-silent region,
      never mid-word.

## 2. Captions

- [ ] Read the full generated `.ass` file text (grep for suspicious
      patterns: literal hyphens inside a word, single-letter lines,
      doubled words) — don't just trust the generator ran without erroring.
      Two concrete patterns hit in production, both easy to miss skimming:
      a hyphenated compound word split across two *consecutive* Dialogue
      lines (e.g. one card ends "...FULL", the next starts "-TIME...") —
      reads as a stray leading hyphen on screen; and the exact same word
      appearing twice in a row in adjacent lines (a Whisper transcription
      duplication artifact, not anything in the actual script). Also check
      for a short caption sitting in what should be an inter-cue silence
      gap (e.g. a stray "1" or single filler word with no corresponding
      script text nearby) — Whisper can hallucinate a word out of near-
      silence/breath noise; cross-reference against `narration.json`'s
      actual text and delete anything that isn't really there.
- [ ] Any acronym pronounced letter-by-letter in the script (e.g. "C-R-M")
      must display as a clean word on screen ("CRM"). This is handled
      automatically by `karaoke.py`'s merge pass — verify it actually fired:
      ```bash
      grep -n -i "your-acronym" captions.ass
      ```
- [ ] Caption ink color matches the current background (dark ink on a
      light background, light ink on a dark background) — check this every
      time the brand palette changes.

## 3. Visual — frame-by-frame beat check

Extract a frame at the midpoint of every cue and Read each one:
```bash
for t in <t1> <t2> <t3> ...; do
  ffmpeg -y -v error -ss $t -i <file>.mp4 -frames:v 1 "qc_$t.png"
done
```
For each frame, check:
- [ ] No duplicate on-screen labels (a `drawtext` layer stacked on top of
      text already baked into an evidence PNG).
- [ ] No dangling/leftover annotation bleeding in from an earlier cue (a
      `hand_box`/`hand_underline` missing its `t_off` upper bound).
- [ ] No frozen/single-frame section (a filter appended without chaining
      `{cur}`).
- [ ] Mascot and any text sit clear of the platform-UI-unsafe zone: below
      `y≈1570` and within ~100px of the right edge on a 1080×1920 canvas.
- [ ] Any text overlaid on a **photoreal** background (hero shots) has
      either a scrim behind it or sits in a genuinely clear region of that
      specific image — don't reuse flat-background text coordinates
      blindly on a busy photo.
- [ ] Flat UI cards are **perfectly static** — no pan, no grain. Camera
      drift/grain should exist ONLY inside photoreal hero segments.
- [ ] Cutaway/real-asset inserts (if any) are topically exact to the
      episode's subject, not a vague mood-word match, and never composited
      under simultaneously-active card text.
- [ ] Typography discipline: max 2 font weights, 1 family per role, max 3
      colors on screen at once (ink + one accent + background).

## 4. Structural / duration

- [ ] `ffprobe` duration of the final render matches the VO's actual
      duration exactly (not the old/assumed `TOTAL`).
- [ ] If the VO was trimmed, confirm every cue timestamp after the cut
      point was shifted by the same delta — a stale timestamp is the most
      common bug after an audio edit. Search `build.py` and the
      `sound-*.json` for any timestamp that looks like it belongs to the
      old duration.

## 5. Brand

- [ ] Palette matches the locked hex values in `brand.md` — spot-check a
      few frames' colors if anything was hand-typed.
- [ ] Mascot pose matches the emotional beat it's placed in (see
      `DESIGN_PHILOSOPHY.md` §4/§3 one-anchor principle).
- [ ] Ends on exactly one locked CTA (see `brand.md`), logged in `_ideas.md`.

## 6. Before declaring "posting ready"

- [ ] Copy the final muxed file into `<episode>/delivery/<episode>-vX.Y-FINAL.mp4`
      — never hand back a path inside the working directory as "the final."
- [ ] State plainly which checklist items were run and which (if any) were
      skipped and why — don't silently skip QC steps under time pressure.
