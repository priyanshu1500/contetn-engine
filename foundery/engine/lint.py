"""DocReel taste/rhythm lint. Usage: python lint.py <episode>/build/edl.json

Checks (generic, engine-level — not episode-specific):
1. One effect per cut (whip + flash together on the same cut).
2. Minimum holds per shot kind (evidence/title/cta need a beat to read).
3. No shot longer than ~14s without a new visual element (attention decay).
4. Same real-world subject+setting back-to-back (set shot.subject/shot.setting to check).
5. Caption chunks stay to 1-2 words (word-by-word rhythm).
6. Energy-rhythm (the "breathing" rule from the visual-language review): flag 3+ consecutive
   shots tagged with the same shot.energy, and flag any 18s window with no 'pause' beat.
7. Relief/pop-culture clip density: shot.relief=True clips must be 1-3s and at most one per 30s
   (the accepted policy for Hollywood emotion-tagged clips — see emotion_clips.py).
"""
import json, sys

d = json.load(open(sys.argv[1] if len(sys.argv) > 1 else 'edl.json', encoding='utf8'))
shots = sorted(d['shots'], key=lambda s: s['t0'])
warns = []

MIN_HOLD = {'evidence': 0.9, 'title': 1.0, 'cta': 1.2, 'wordcard': 0.9, 'stat': 1.0, 'year': 1.0, 'label': 1.0}
for s in shots:
    dur = s['t1'] - s['t0']
    m = MIN_HOLD.get(s['kind'], 0.18)
    if dur < m:
        warns.append(f'{s["id"]} ({s["kind"]}): hold {dur:.2f}s < {m}s minimum')
    if dur > 14:
        warns.append(f'{s["id"]}: shot holds {dur:.2f}s with no new visual element (>14s)')

flashes = d.get('flashes', [])
for a, b in zip(shots, shots[1:]):
    fx = []
    if b.get('whip'): fx.append('whip')
    if any(abs(b['t0'] - x) < 0.06 for x in flashes): fx.append('flash')
    if b.get('flicker') and b.get('duotone'): pass  # flicker+duotone together is one intentional "archival" look, not double-counted
    if len(fx) > 1:
        warns.append(f'{b["t0"]:.2f}s {b["id"]}: {len(fx)} effects on one cut ({fx})')

for a, b in zip(shots, shots[1:]):
    if a.get('subject') and a.get('subject') == b.get('subject') and a.get('setting') == b.get('setting'):
        warns.append(f'{b["id"]}: same subject+setting back-to-back ({a["id"]}->{b["id"]}: {b["subject"]}/{b["setting"]})')

for t in d.get('text', []):
    if t.get('mode') == 'word' and len(t['words']) > 2:
        warns.append(f'caption chunk >2 words at {t["t0"]}s')

# energy rhythm
run = 1
for a, b in zip(shots, shots[1:]):
    if a.get('energy') and a.get('energy') == b.get('energy'):
        run += 1
        if run >= 3: warns.append(f'{b["id"]}: {run} consecutive shots with energy "{b["energy"]}" (breathing rule: alternate hook/evidence/movie/pause/escalation/proof/payoff)')
    else:
        run = 1

has_energy = any(s.get('energy') for s in shots)
if has_energy:
    window = 18.0
    t = shots[0]['t0']
    end = shots[-1]['t1']
    while t < end:
        in_window = [s for s in shots if s['t0'] < t + window and s['t1'] > t]
        if in_window and not any(s.get('energy') == 'pause' for s in in_window):
            warns.append(f'{t:.1f}-{t+window:.1f}s: no "pause" energy beat in this {window:.0f}s window')
        t += window

# relief-clip density (Hollywood emotion-tagged clips — Option C policy: 1-3s, max 1 per 30s)
relief = [s for s in shots if s.get('relief')]
for s in relief:
    dur = s['t1'] - s['t0']
    if not (1.0 <= dur <= 3.0):
        warns.append(f'{s["id"]}: relief clip is {dur:.2f}s, must be 1-3s per the accepted policy')
for a, b in zip(relief, relief[1:]):
    if b['t0'] - a['t0'] < 30:
        warns.append(f'relief clips too close: {a["id"]}@{a["t0"]:.1f}s and {b["id"]}@{b["t0"]:.1f}s (< 30s apart)')

print('\n'.join(warns) if warns else 'lint: clean')
print(f'{len(warns)} warning(s); {len(shots)} shots')
