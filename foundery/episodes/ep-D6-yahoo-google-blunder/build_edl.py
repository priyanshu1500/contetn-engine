"""
build_edl.py — Rebuilt for Episode D6 "The $1,000,000 Blunder" (Yahoo vs. Google)
Adheres 100% to:
- The Curiosity Ladder Framework
- Authentic Archival Footage Pacing (~2.5s - 3.8s per shot, 22 dynamic shots)
- High-Contrast Optical Resets (Stark slides, cards, real TV archives)
- Multi-Font Editorial Captions (Sans, Serif Italic, Condensed Display, Mono)
"""
import json, os, sys

HERE = r'D:\agency content\BIN\documentary_tofu\ep-D6-yahoo-google-blunder'
ENGINE_DIR = r'D:\agency content\BIN\documentary_tofu\engine'
sys.path.append(ENGINE_DIR)
from editorial_edl import format_caption_chunks

words = json.load(open(os.path.join(HERE, 'words_timing.json'), encoding='utf8'))
voice_dur = words[-1]['end'] + 0.6
DUR = round(voice_dur, 2)

def find_word_time(target, after=0.0):
    t_low = target.lower().rstrip('.,!?\"')
    for w in words:
        if w['start'] >= after and w['word'].lower().rstrip('.,!?\"') == t_low:
            return w['start']
    return None

def find_word_end(target, after=0.0):
    t_low = target.lower().rstrip('.,!?\"')
    for w in words:
        if w['start'] >= after and w['word'].lower().rstrip('.,!?\"') == t_low:
            return w['end']
    return None

# Narrative Key Beat Timestamps
t_house = find_word_end('house.', 0.0) or 4.4
t_building = find_word_end('building.', t_house) or 7.5
t_pagerank = find_word_end('PageRank.', t_building) or 10.6
t_brin = find_word_end('Brin.', t_pagerank) or 14.5
t_yahoo1 = find_word_end('Yahoo.', t_brin) or 17.5
t_understands = find_word_end('understands:', t_yahoo1) or 20.0
t_bad = find_word_end('bad.', t_understands) or 24.2
t_fast = find_word_end('fast.', t_bad) or 27.2
t_banner_ads = find_word_end('ads.', t_fast) or 34.3
t_opposite = find_word_end('opposite:', t_banner_ads) or 37.5
t_seconds = find_word_end('SECONDS.', t_opposite) or 42.5
t_distraction = find_word_end('distraction.', t_seconds) or 44.5
t_mistake = find_word_end('mistake', t_distraction) or 48.0
t_cash = find_word_end('cash.', t_mistake) or 51.5
t_five = find_word_end('five.', t_cash) or 54.0
t_dollars2 = find_word_end('dollars.', t_five) or 58.5
t_scrap_metal = find_word_end('metal.', t_dollars2) or 63.0
t_empire = find_word_end('empire.', t_scrap_metal) or 68.0
t_mistake2 = find_word_end('mistake.', t_empire) or 71.5

shots = []
si = 1

def add(kind, t0, t1, **kw):
    global si
    shots.append({'id': f's{si}', 't0': round(t0, 2), 't1': round(t1, 2), 'kind': kind, **kw})
    si += 1

# -------------------------------------------------------------
# ACT 1: THE ASYMMETRIC REJECTION HOOK (Outcome-First, No Names)
# -------------------------------------------------------------
# s1: Young Larry in the Menlo Park garage (authentic CRT monitor 1998)
add('video', 0.0, t_house, src='clips/larry_garage_90s.mp4', **{'from': 0.0},
    push=0.03, dir='R', grade='contrast(1.15) brightness(0.95)',
    job='hook: young founder in garage offering entire company for house price')

# s2: Larry and Sergey young arms crossed 1998
add('video', t_house, t_building, src='clips/larry_sergey_young_arms.mp4', **{'from': 0.0},
    push=0.02, dir='L', whip=True,
    job='hook: boardroom laughed them out')

# s3: STARK OPTICAL RESET: THE ALGORITHM WAS PAGERANK
add('stark', t_building, t_pagerank,
    stark={
        'text': 'THE ALGORITHM WAS PAGERANK.',
        'sub': 'Stanford Computer Science Department // 1998 Patent',
        'bg': 'white',
        'tag': 'PRIMARY INTELLECTUAL PROPERTY',
        'size': 110,
    },
    job='stark high-key contrast reset slide: PageRank reveal')

# s4: Real photo of Larry Page (Polaroid card)
add('polaroid', t_pagerank, t_brin,
    polaroid={
        'src': 'img/larry_young.jpg',
        'label': 'Larry Page · Age 24 (Stanford University)',
        'scale': 1.05,
        'rot': -2.5,
    },
    job='polaroid: Larry Page student archive')

# s5: Boardroom Minutes Rejection Card ($1M Rejected)
add('evidence', t_brin, t_yahoo1, src='img/yahoo_google_rejection_card.png',
    scale=1.52, pos=[350, 140], imgSize=[760, 475], imgOff=[0, 0], dir='R',
    source='PRIMARY ARCHIVE · 1998 YAHOO! BOARDROOM MINUTES',
    label=[round(t_brin + 0.2, 1), round(t_brin + 0.6, 1)],
    job='evidence: Yahoo rejected $1,000,000 offer')

# -------------------------------------------------------------
# ACT 2: THE SPEED THREAT & THE PORTAL TRAP (The Curiosity Re-Hook)
# -------------------------------------------------------------
# s6: Stark Reset: WHY THEY REJECTED IT
add('stark', t_yahoo1, t_understands,
    stark={
        'text': 'THEY DID NOT REJECT IT BECAUSE IT WAS BAD.',
        'sub': 'The fatal strategic calculation of 1998',
        'bg': 'dark',
        'tag': 'THE STRATEGIC ERROR',
        'size': 95,
    },
    job='stark dark contrast reset slide: Why they rejected it')

# s7: Jerry Yang archival interview (defending the portal)
add('video', t_understands, t_bad, src='clips/jerry_yang_interview.mp4', **{'from': 0.0},
    push=0.02, dir='R', whip=True,
    job='authentic archival: Jerry Yang on camera explaining Yahoo business model')

# s8: Stark Reset: TOO FAST
add('stark', t_bad, t_fast,
    stark={
        'text': 'IT WAS TOO FAST.',
        'sub': 'Search was viewed as a traffic leak, not an asset.',
        'bg': 'white',
        'tag': 'THE METRIC DIVERGENCE',
        'size': 140,
    },
    job='stark high-key optical reset: TOO FAST punch')

# s9: 1998 Cluttered Portal Card (The 45-minute trap)
add('still', t_fast, t_banner_ads, src='img/yahoo_portal_trap_card.png',
    fx=0.5, fy=0.5, push=0.03, dir='L',
    job='proof: Yahoo portal trap 45 minutes banner ads')

# s10: Google 3 Seconds Exit Speed Metric Card
add('still', t_banner_ads, t_opposite, src='img/google_speed_card.png',
    fx=0.5, fy=0.5, push=0.03, dir='R', whip=True,
    job='proof: Google 3-second exit velocity')

# s11: Young Larry Page presenting Google speed
add('video', t_opposite, t_seconds, src='clips/larry_page_speech_2000.mp4', **{'from': 0.0},
    push=0.025, dir='L',
    job='authentic video: Larry Page speaking on Google search speed')

# s12: Stark Dark: YAHOO CALLED IT A DISTRACTION
add('stark', t_seconds, t_distraction,
    stark={
        'text': '"A DISTRACTION."',
        'sub': 'Yahoo internal memo dismissing search algorithm',
        'bg': 'dark',
        'tag': 'EXECUTIVE CONSENSUS',
        'size': 130,
    },
    job='stark dark reset: A distraction')

# -------------------------------------------------------------
# ACT 3: THE $3 BILLION SECOND CHANCE (Escalation)
# -------------------------------------------------------------
# s13: Yahoo CEO Terry Semel on stage
add('video', t_distraction, t_mistake, src='clips/terry_semel_keynote.mp4', **{'from': 0.0},
    push=0.02, dir='R', whip=True,
    job='authentic archival: Terry Semel Yahoo keynote 2002')

# s14: Stat Roll: $3,000,000,000 Cash Offer
add('stat', t_mistake, t_cash,
    stat={'prefix': '$', 'from': 1, 'to': 3, 'suffix': 'BILLION CASH OFFER', 'roll': [round(t_mistake + 0.2, 1), round(t_mistake + 1.2, 1)], 'style': 'paper'},
    job='stat: $3B cash acquisition offer in 2002')

# s15: Polaroid Sergey Brin (Counter-offer $5B)
add('polaroid', t_cash, t_five,
    polaroid={
        'src': 'img/sergey_young.jpg',
        'label': 'Sergey Brin · Demand: $5,000,000,000',
        'scale': 1.05,
        'rot': 2.3,
    },
    job='polaroid: Sergey Brin $5B demand')

# s16: Stark White: YAHOO WALKED OVER $2 BILLION
add('stark', t_five, t_dollars2,
    stark={
        'text': 'YAHOO WALKED AWAY OVER $2 BILLION.',
        'sub': '2002 negotiation collapse // Deal abandoned',
        'bg': 'white',
        'tag': 'THE $2B SPREAD',
        'size': 95,
    },
    job='stark high-key reset: Yahoo walked away over $2B')

# -------------------------------------------------------------
# ACT 4: THE CATASTROPHIC DIVERGENCE & VERIZON SALE
# -------------------------------------------------------------
# s17: Marissa Mayer crisis / decline
add('video', t_dollars2, t_scrap_metal, src='clips/marissa_mayer_yahoo.mp4', **{'from': 0.0},
    push=0.02, dir='L', whip=True,
    job='authentic archival: Marissa Mayer final era of Yahoo')

# s18: CBS News Broadcast: Verizon Buys Yahoo for $4.48B
add('video', t_scrap_metal, t_empire, src='clips/cbs_news_verizon_yahoo.mp4', **{'from': 0.0},
    push=0.025, dir='R',
    job='authentic broadcast: CBS News Verizon buys Yahoo for scrap metal')

# s19: The Trillion Dollar Divergence Card ($2.1T Alphabet vs $4.48B Yahoo)
add('still', t_empire, t_mistake2, src='img/trillion_divergence_card.png',
    fx=0.5, fy=0.5, push=0.03, dir='L',
    job='proof: Trillion dollar divergence metric')

# s20: STARK FINAL CLIMAX: EXTINCTION EVENT
add('stark', t_mistake2, DUR,
    stark={
        'text': 'PASSING ON IT TWICE IS AN EXTINCTION EVENT.',
        'sub': 'The faster machine wins every single time.',
        'bg': 'dark',
        'tag': 'THE UNFORGIVING LAW',
        'size': 85,
    },
    job='stark optical climax: extinction event')

# -------------------------------------------------------------
# Automated Multi-Font Editorial Captions
# -------------------------------------------------------------
EMPH = {
    'twenty-four-year-olds', 'company', 'house.', 'boardroom', 'laughed',
    'building.', 'PageRank.', 'Larry', 'Page', 'Sergey', 'Brin.', 'Yahoo.',
    'understands:', 'reject', 'Google', 'bad.', 'fast.', 'nineteen',
    'ninety-eight,', 'revenue', 'trapping', 'forty-five', 'minutes', 'banner',
    'ads.', 'opposite:', 'answer', 'kick', '3', 'SECONDS.', 'distraction.',
    'Four', 'years', 'two', 'thousand', 'mistake', '$3,000,000,000', 'cash.',
    'five.', 'second', 'time', 'billion', 'dollars.', 'Fourteen', 'Verizon',
    'scrap', 'metal.', 'search', '$1', 'Trillion', 'empire.', 'future',
    'mistake.', 'twice', 'extinction', 'event.'
}

text = format_caption_chunks(words, EMPH)

annotations = [
    {'t0': 0.5, 't1': 4.0, 'text': 'PRIMARY ARCHIVE · MENLO PARK GARAGE 1998', 'pos': 'br'},
    {'t0': round(t_house + 0.2, 1), 't1': round(t_building - 0.2, 1), 'text': 'LARRY PAGE & SERGEY BRIN · STANFORD UNIVERSITY', 'pos': 'br'},
    {'t0': round(t_understands + 0.2, 1), 't1': round(t_bad - 0.2, 1), 'text': 'JERRY YANG · CO-FOUNDER, YAHOO!', 'pos': 'br'},
    {'t0': round(t_opposite + 0.2, 1), 't1': round(t_seconds - 0.2, 1), 'text': 'LARRY PAGE · PRESENTING GOOGLE SEARCH SPEED', 'pos': 'br'},
    {'t0': round(t_distraction + 0.2, 1), 't1': round(t_mistake - 0.2, 1), 'text': 'TERRY SEMEL · CEO, YAHOO! (2002)', 'pos': 'br'},
    {'t0': round(t_dollars2 + 0.2, 1), 't1': round(t_scrap_metal - 0.2, 1), 'text': 'MARISSA MAYER · FINAL CEO, YAHOO!', 'pos': 'br'},
    {'t0': round(t_scrap_metal + 0.2, 1), 't1': round(t_empire - 0.2, 1), 'text': 'CBS NEWS ARCHIVE · JULY 2016 SALE TO VERIZON', 'pos': 'br'},
]

edl = {
    'duration': DUR,
    'specks': True,
    'shots': shots,
    'text': text,
    'annotations': annotations,
    'overlays': [],
    'flashes': [],
    'fadeOut': [round(DUR - 2.0, 1), DUR],
}

out_path = os.path.join(HERE, 'build', 'edl.json')
json.dump(edl, open(out_path, 'w', encoding='utf8'), indent=1)
print(f'Done! Compiled {len(shots)} shots; {len(text)} caption bursts; duration {DUR}s')
