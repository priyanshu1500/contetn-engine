"""Build edl.json for Episode D3 v2 — "The One-Person Billion Dollar Company"
MetroMedia Gold Standard with correct transcription fixes (e.g. Kerser -> Cursor).
"""
import json, os

HERE = r'D:\agency content\BIN\documentary_tofu\ep-D3-one-person-unicorn'
words = json.load(open(os.path.join(HERE, 'words_timing_v2.json'), encoding='utf8'))

# Word fixes for Whisper transcription errors
FIX = {
    'Kerser': 'Cursor',
    'kerser': 'Cursor',
    'Kerser.': 'Cursor.',
    'kerser.': 'Cursor.',
    'superintelligence': 'Superintelligence',
    'superintelligence.': 'Superintelligence.',
}
for w in words:
    w['word'] = FIX.get(w['word'], w['word'])

# Clean up split number/hyphen words if any (e.g. stand -up -> standup)
i = 0
while i < len(words) - 1:
    if words[i]['word'] == 'stand' and words[i + 1]['word'] in ('-up', 'up'):
        words[i]['word'] = 'standup'
        words[i]['end'] = words[i + 1]['end']
        del words[i + 1]
    elif words[i]['word'] == '10' and words[i + 1]['word'] in (',000', '000'):
        words[i]['word'] = '10,000'
        words[i]['end'] = words[i + 1]['end']
        del words[i + 1]
    else:
        i += 1

voice_dur = words[-1]['end'] + 0.6
DUR = round(voice_dur, 1)

def find_word_time(target, after=0.0):
    target_lower = target.lower().rstrip('.,!?')
    for w in words:
        if w['start'] >= after and w['word'].lower().rstrip('.,!?') == target_lower:
            return w['start']
    return None

def find_sentence_end(keyword, after=0.0):
    target_lower = keyword.lower().rstrip('.,!?')
    for i, w in enumerate(words):
        if w['start'] >= after and w['word'].lower().rstrip('.,!?') == target_lower:
            for j in range(i, min(i + 15, len(words))):
                if words[j]['word'].endswith(('.', '!', '?')):
                    return words[j]['end']
            return w['end']
    return None

# Whisper word timestamps
t_panic = find_sentence_end('panic', 0.0) or 4.8
t_billion_w = find_word_time('billion', 3.0) or 6.5
t_no_team = find_sentence_end('team', t_panic) or 9.5
t_happening = find_sentence_end('happening', t_no_team) or 11.5
t_cursor = find_word_time('Cursor', t_happening - 1) or 14.0
t_fifty = find_sentence_end('50', t_cursor) or find_sentence_end('fifty', t_cursor) or 18.0
t_twenty = find_sentence_end('20', t_fifty) or find_sentence_end('twenty', t_fifty) or 23.0

# ACT 3: THE TURN
t_telling = find_sentence_end('you', 23.0) or 25.1
t_humans = find_sentence_end('humans', t_telling) or 29.6
t_work = find_sentence_end('work', t_humans) or 35.1
t_meetings = find_sentence_end('meetings', t_work) or 38.0
t_reports = find_sentence_end('reports', t_meetings) or 40.5
t_half = find_sentence_end('half', t_reports) or 44.0

# ACT 4: DEPTH
t_glue = find_sentence_end('glue', t_half) or 47.0
t_agents = find_sentence_end('code', t_glue) or 51.0
t_standup = find_sentence_end('meeting', t_agents) or 56.0
t_roof = find_sentence_end('roof', t_standup) or 60.0
t_thousand = find_sentence_end('thousand', t_roof) or 63.8

# ACT 5: PROVOCATION
t_jensen = find_word_time('Jensen', t_thousand - 1) or 64.0
t_jensen_mid = round(t_jensen + 3.2, 2)
t_models = find_sentence_end('models', t_jensen) or 70.0
t_betting = find_sentence_end('future', t_models) or 73.5
t_coming = find_sentence_end('coming', t_betting) or 76.5

shots = []
si = 1

def add(kind, t0, t1, **kw):
    global si
    shots.append({'id': f's{si}', 't0': round(t0, 2), 't1': round(t1, 2), 'kind': kind, **kw})
    si += 1

# ------------------------------------------------------------------ ACT 1: SHOCK HOOK
# s1: Altman on camera (Pristine 1080p full color)
add('video', 0.0, t_panic, src='clips/altman_close.mp4', **{'from': 0.0}, push=0.025, dir='R',
    job='hook: real Sam Altman on camera close-up')

# s2: $1B rolling counter
add('stat', t_panic, t_happening,
    stat={'prefix': '$', 'from': 0, 'to': 1000000000, 'roll': [round(t_panic + 0.4, 1), round(t_billion_w + 0.8, 1)], 'style': 'paper'},
    job='stat: $1B rolling counter')

# ------------------------------------------------------------------ ACT 2: ESCALATION
# s3: Altman reaction cutaway (full color)
add('video', t_happening, t_cursor - 0.2, src='clips/altman_reaction.mp4', **{'from': 0.5},
    push=0.025, dir='L', whip=True, job='real Sam Altman reaction cutaway')

# s4: Sacra Data Card (Cursor $100M ARR)
add('evidence', t_cursor - 0.2, t_fifty, src='img/sacra_data_card.png',
    scale=1.55, pos=[350, 140], imgSize=[760, 475], imgOff=[0, 0], dir='R',
    source='DATA · PITCHBOOK & SACRA RESEARCH · TINY TEAM UNICORNS',
    label=[round(t_cursor + 0.3, 1), round(t_cursor + 0.7, 1)],
    job='evidence: real Sacra data card (Cursor $100M ARR)')

# s5: Business Insider Card (SSI $32B / 20 staff)
add('evidence', t_fifty, t_twenty, src='img/bi_altman_card.png',
    scale=1.55, pos=[350, 140], imgSize=[760, 475], imgOff=[0, 0], dir='L',
    source='SOURCE · BUSINESS INSIDER · REBECCA TORRENCE · MAY 7 2025',
    label=[round(t_fifty + 0.3, 1), round(t_fifty + 0.7, 1)],
    job='evidence: real Business Insider article')

# ------------------------------------------------------------------ ACT 3: THE TURN (Rich Cinematic Palette)
# s6: Altman Senate Testimony (The Turn - Full Color Broadcast)
add('video', t_twenty, t_telling, src='clips/altman_bloomberg.mp4', **{'from': 4.0},
    push=0.03, dir='L', whip=True,
    job='THE TURN: real Altman Senate testimony on Capitol Hill')

# s7: OpenAI HQ San Francisco exterior
add('video', t_telling, t_humans, src='clips/openai_sign.mp4', **{'from': 0.0},
    push=0.03, dir='R', whip=True,
    job='OpenAI San Francisco HQ press conference')

# s8: Corporate Labor Thesis Card
add('evidence', t_humans, t_work, src='img/leverage_thesis_card.png',
    scale=1.55, pos=[350, 140], imgSize=[760, 475], imgOff=[0, 0], dir='R',
    source='LABOR ECONOMICS · HARVARD BUSINESS REVIEW',
    label=[round(t_humans + 0.3, 1), round(t_humans + 0.7, 1)],
    job='evidence: corporate labor vs coordination thesis')

# s9: Coordination Drag Card
add('evidence', t_work, t_meetings, src='img/coordination_drag_card.png',
    scale=1.55, pos=[350, 140], imgSize=[760, 475], imgOff=[0, 0], dir='L',
    source='COORDINATION OVERHEAD · SILICON VALLEY BENCHMARK',
    label=[round(t_work + 0.3, 1), round(t_work + 0.7, 1)],
    job='evidence: coordination overhead stat card')

# s10: Silicon Valley tech campus (Full Color 1080p aerial)
add('video', t_meetings, t_reports, src='clips/tech_campus.mp4', **{'from': 15.0},
    push=0.02, dir='R', whip=True,
    job='real Silicon Valley tech campus drone — natural color')

# s11: Altman reaction (keeps human face presence)
add('video', t_reports, t_half, src='clips/altman_reaction.mp4', **{'from': 1.0},
    push=0.025, dir='L', whip=True,
    job='Altman reaction — organizational collapse')

# ------------------------------------------------------------------ ACT 4: DEPTH & PROOF
# s12: Altman close reflection (AI kills the glue)
add('video', t_half, t_glue, src='clips/altman_close.mp4', **{'from': 2.0},
    push=0.025, dir='R', whip=True,
    job='Altman close-up — AI kills the glue')

# s13: Real Cursor AI IDE demo (Full HD code generation)
add('video', t_glue, t_agents, src='clips/cursor_ide.mp4', **{'from': 0.0},
    push=0.02, dir='L', whip=True,
    job='real Cursor AI IDE demo — autonomous agents writing code')

# s14: Reuters tech report (ChatGPT & AI automation workflows)
add('video', t_agents, t_standup, src='clips/chatgpt_reuters.mp4', **{'from': 8.0},
    push=0.025, dir='R', whip=True,
    job='Reuters AI automation footage — 24/7 compliance & support')

# s15: OpenAI HQ exterior (Modern high-tech architecture)
add('video', t_standup, t_roof, src='clips/openai_sign.mp4', **{'from': 2.0},
    push=0.025, dir='L', whip=True,
    job='OpenAI headquarters exterior — modern AI enterprise')

# s16: Stat Counter #2 (1 -> 10,000 leverage)
add('stat', t_roof, t_jensen,
    stat={'prefix': '', 'from': 1, 'to': 10000, 'suffix': 'PEOPLE', 'roll': [round(t_roof + 0.3, 1), round(t_roof + 2.0, 1)], 'style': 'dark'},
    job='stat: 1 -> 10,000 people leverage counter')

# ------------------------------------------------------------------ ACT 5: PROVOCATION & CLOSE
# s17: Jensen Huang Keynote (4K/1080p full color)
add('video', t_jensen, t_jensen_mid, src='clips/jensen_keynote.mp4', **{'from': 0.0},
    push=0.025, dir='L', whip=True,
    job='real Jensen Huang NVIDIA keynote — $13B Hugging Face deal')

# s18: Reuters AI developer ecosystem footage
add('video', t_jensen_mid, t_models, src='clips/chatgpt_reuters.mp4', **{'from': 2.0},
    push=0.025, dir='R', whip=True,
    job='Reuters AI platform cutaway — open source model ecosystems')

# s19: $13 BILLION stat counter
add('stat', t_models, t_betting,
    stat={'prefix': '$', 'from': 0, 'to': 13, 'suffix': 'BILLION', 'roll': [round(t_models + 0.2, 1), round(t_models + 1.5, 1)], 'style': 'dark'},
    job='stat: $13B acquisition counter')

# s20: Altman Senate Testimony (Decisive leadership)
add('video', t_betting, t_coming, src='clips/altman_bloomberg.mp4', **{'from': 8.0},
    push=0.025, dir='L', whip=True,
    job='Sam Altman testifying on AI disruption')

# s21: Altman closing reflection fading to black
add('video', t_coming, DUR, src='clips/altman_reflection.mp4', **{'from': 0.5},
    push=0.02, dir='R',
    job='close: real Sam Altman reflection fading to black')

# ------------------------------------------------------------------ captions
EMPH = {'panic.', 'company.', 'team.', 'happening.', 'Cursor', 'revenue', 'people.', 'twenty.',
        'telling', 'you.', 'humans.', 'work.', 'coordination.', 'meetings.', 'reports.',
        'half.', 'glue.', 'standup', 'meeting.', 'roof.', 'thousand.', 'models.', 'future.',
        'one.', 'one,', 'thirteen', 'billion', 'dollars'}

chunks, cur = [], []
def flush():
    global cur
    if cur:
        chunks.append(cur)
        cur = []

for w in words:
    cur.append(w)
    if len(cur) >= 3 or w['word'].rstrip('.,!?') in EMPH or w['word'].endswith(('.', '!', '?')):
        flush()
flush()

text = []
for i, ch in enumerate(chunks):
    t0 = ch[0]['start']
    nxt = chunks[i + 1][0]['start'] if i + 1 < len(chunks) else DUR
    t1 = min(ch[-1]['end'] + 0.22, nxt if nxt - t0 < 1.4 else t0 + 1.4)
    t1 = min(max(t1, t0 + 0.28), nxt)
    
    chunk_words = []
    for w in ch:
        color = '#F5C542' if w['word'].rstrip('.,!?') in {e.rstrip('.,!?') for e in EMPH} else '#FFFFFF'
        chunk_words.append({'w': w['word'], 't': round(w['start'], 3), 'color': color})
    
    text.append({'t0': round(t0, 3), 't1': round(t1, 3), 'mode': 'word', 'words': chunk_words})

annotations = [
    {'t0': 0.2, 't1': round(t_panic - 0.3, 1), 'text': 'SAM ALTMAN · CEO, OPENAI', 'pos': 'br'},
    {'t0': round(t_twenty + 0.3, 1), 't1': round(t_telling - 0.3, 1), 'text': 'U.S. SENATE TESTIMONY · CAPITOL HILL', 'pos': 'br'},
    {'t0': round(t_jensen + 0.3, 1), 't1': round(t_jensen_mid - 0.3, 1), 'text': 'JENSEN HUANG · CEO, NVIDIA', 'pos': 'br'},
]

edl = {
    'duration': DUR,
    'specks': True,
    'shots': shots,
    'text': text,
    'annotations': annotations,
    'overlays': [],
    'flashes': [],
    'fadeOut': [round(DUR - 2.5, 1), DUR],
}

out_path = os.path.join(HERE, 'build', 'edl.json')
json.dump(edl, open(out_path, 'w', encoding='utf8'), indent=1)
print(f'Done! {len(shots)} shots; {len(text)} caption chunks; duration {DUR}s')
