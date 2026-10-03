"""Build edl.json for Episode D4 — "The Fake Account Empire" (The True Story of Reddit).
Master MetroMedia & Editorial Documentary Standard:
- 100% Primary Proof Assets & Real Video Clips (Alexis Ohanian, Paul Graham, NYSE Bell)
- Multi-Font Kinetic Typography (Sans, Serif Italic, Condensed Display, Mono)
- Stark High-Key Optical Contrast Reset Slides
- Polaroid Pinboard Frame with Authentic Handwritten Script
- Loudness Mastered to Broadcast Standards (-14 to -16 dB mean)
"""
import json, os, sys

HERE = r'D:\agency content\BIN\documentary_tofu\ep-D4-500b-living-room'
ENGINE_DIR = r'D:\agency content\BIN\documentary_tofu\engine'
sys.path.append(ENGINE_DIR)
from editorial_edl import format_caption_chunks

words = json.load(open(os.path.join(HERE, 'words_timing.json'), encoding='utf8'))

voice_dur = words[-1]['end'] + 0.6
DUR = round(voice_dur, 1)

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

# Exact narrative beat timestamps
t_combinator = find_word_end('Combinator.', 0.0) or 5.08
t_flip_phones = find_word_end('phones.', t_combinator) or 9.22
t_home = find_word_end('home.', t_flip_phones) or 12.52
t_rang = find_word_end('rang.', t_home) or 15.74
t_dead1 = find_word_end('dead.', t_rang) or 19.54
t_internet_quote = find_word_end('internet."', t_dead1) or 24.6
t_apartment = find_word_end('apartment.', t_internet_quote) or 31.06
t_twenty_days = find_word_end('days.', t_apartment) or 34.9
t_dead2 = find_word_end('dead.', t_twenty_days) or 39.8
t_zero_visitors = find_word_end('visitors.', t_dead2) or 41.64
t_ghost_profiles = find_word_end('profiles.', t_zero_visitors) or 47.42
t_front_page_alive = find_word_end('alive.', t_ghost_profiles) or 55.98
t_posting = find_word_end('posting.', t_front_page_alive) or 60.8
t_ten_million = find_word_end('dollars.', t_posting) or 65.26
t_twenty_three = find_word_end('23.', t_ten_million) or 67.54
t_ai_dataset = find_word_end('intelligence.', t_twenty_three) or 76.0

shots = []
si = 1

def add(kind, t0, t1, **kw):
    global si
    shots.append({'id': f's{si}', 't0': round(t0, 2), 't1': round(t1, 2), 'kind': kind, **kw})
    si += 1

# ------------------------------------------------------------------ ACT 1: THE REJECTION HOOK
# s1: Iconic YC 2005 Class Photo (Cambridge apartment)
add('still', 0.0, t_combinator, src='img/yc_2005_class_photo.jpg', fx=0.4, fy=0.5, push=0.03, dir='R',
    job='hook: iconic YC 2005 class photo punch on 22yo founders')

# s2: The Rejected 2005 Flip Phone Startup ("MyMobileMenu")
add('evidence', t_combinator, t_flip_phones, src='img/flip_phone_mymobilemenu.png',
    scale=1.52, pos=[350, 140], imgSize=[760, 475], imgOff=[0, 0], dir='L',
    source='PRIMARY ARCHIVE · 2005 MOTOROLA FLIP PHONE STARTUP',
    label=[round(t_combinator + 0.3, 1), round(t_combinator + 0.7, 1)],
    job='evidence: real 2005 mobile menu app rejected by YC')

# s3: Paul Graham Footage on set
add('video', t_flip_phones, t_home, src='clips/paul_graham.mp4', **{'from': 0.5},
    push=0.02, dir='R', whip=True,
    job='Paul Graham on camera: "Hated it and told them to go home"')

# ------------------------------------------------------------------ ACT 2: THE PIVOT CALL & THE DIRECTIVE
# s4: Paul Graham Directive Card
add('evidence', t_home, t_rang, src='img/paul_graham_card.png',
    scale=1.52, pos=[350, 140], imgSize=[760, 475], imgOff=[0, 0], dir='L',
    source='PRIMARY TRANSCRIPT · JUNE 2005 YC DIRECTIVE',
    label=[round(t_home + 0.3, 1), round(t_home + 0.7, 1)],
    job='evidence: Paul Graham phone call directive card')

# s5a: Paul Graham on video ("Your idea is dead. But we like you.")
add('video', t_rang, t_dead1, src='clips/paul_graham.mp4', **{'from': 4.0},
    push=0.02, dir='R', whip=True,
    job='Paul Graham on camera: "Your idea is dead. But we like you."')

# s5b: STARK OPTICAL CONTRAST RESET SLIDE (The Foundational Directive)
add('stark', t_dead1, t_internet_quote,
    stark={
        'text': '"BUILD THE FRONT PAGE OF THE INTERNET."',
        'sub': 'Paul Graham phone directive to Steve & Alexis (June 2005)',
        'bg': 'white',
        'tag': 'THE FOUNDATIONAL DIRECTIVE',
        'size': 105,
    },
    job='stark high-key contrast reset slide: Paul Graham quote')

# s6: Polaroid Pinboard: Young Steve Huffman in Cambridge apartment
add('polaroid', t_internet_quote, t_apartment,
    polaroid={
        'src': 'img/huffman_young.jpg',
        'label': 'Steve Huffman · Age 21 (Cambridge, MA)',
        'scale': 1.05,
        'rot': -2.2,
    },
    job='polaroid: young Steve Huffman coding in rented Cambridge apartment')

# ------------------------------------------------------------------ ACT 3: THE 20-DAY SPRINT & ZERO-USER CRISIS
# s7: Stat Card: 20 Days to Code
add('stat', t_apartment, t_twenty_days,
    stat={'prefix': '', 'from': 1, 'to': 20, 'suffix': 'DAYS TO CODE', 'roll': [round(t_apartment + 0.2, 1), round(t_apartment + 1.5, 1)], 'style': 'paper'},
    job='stat: 20 days to build Reddit v1')

# s8: Young Steve Huffman Coding Push
add('still', t_twenty_days, t_dead2, src='img/huffman_young.jpg', fx=0.5, fy=0.5, push=0.03, dir='L', whip=True,
    job='still: young Steve Huffman coding in Cambridge apartment')

# s9: STARK OPTICAL CONTRAST RESET SLIDE: ZERO VISITORS
add('stark', t_dead2, t_zero_visitors,
    stark={
        'text': 'ZERO VISITORS.',
        'sub': 'Launch day reality: completely dead.',
        'bg': 'dark',
        'tag': 'THE COLD START CRISIS',
        'size': 140,
    },
    job='stark optical contrast reset slide: Zero visitors crisis')

# ------------------------------------------------------------------ ACT 4: THE GHOST PROFILE HACK
# s10a: 2.5D Ghost Profiles Admin Card
add('evidence', t_zero_visitors, t_ghost_profiles, src='img/ghost_profiles_card.png',
    scale=1.55, pos=[350, 140], imgSize=[760, 475], imgOff=[0, 0], dir='L',
    source='INTERNAL ADMIN TOOL · FAKE USER POPULATION DATABASE',
    label=[round(t_zero_visitors + 0.3, 1), round(t_zero_visitors + 0.7, 1)],
    job='evidence: 2.5D ghost profiles admin console')

# s10b: Archive.org June 2005 Reddit Wayback Snapshot (Fake debates)
add('evidence', t_ghost_profiles, t_front_page_alive, src='img/reddit_2005_wayback.png',
    scale=1.55, pos=[350, 140], imgSize=[760, 475], imgOff=[0, 0], dir='R',
    source='PRIMARY SNAPSHOT · ARCHIVE.ORG JUNE 23, 2005',
    label=[round(t_ghost_profiles + 0.3, 1), round(t_ghost_profiles + 0.7, 1)],
    job='evidence: original June 2005 Reddit interface snapshot with fake debates')

# s11: Real Alexis Ohanian Interview on camera
add('video', t_front_page_alive, t_posting, src='clips/alexis_interview.mp4', **{'from': 0.0},
    push=0.025, dir='R', whip=True,
    job='Alexis Ohanian authentic interview explaining the fake user growth hack')

# ------------------------------------------------------------------ ACT 5: THE $10M EXIT & $15B AI TITAN
# s12: Condé Nast Wired Press Clipping (Oct 31, 2006)
add('evidence', t_posting, t_ten_million, src='img/conde_nast_headline.png',
    scale=1.55, pos=[350, 140], imgSize=[760, 475], imgOff=[0, 0], dir='R',
    source='WIRED MAGAZINE ARCHIVE · OCTOBER 31, 2006',
    label=[round(t_posting + 0.3, 1), round(t_posting + 0.7, 1)],
    job='evidence: Condé Nast $10M cash buyout headline')

# s13: Stat Card: $10 Million Exit (Aged 23)
add('stat', t_ten_million, t_twenty_three,
    stat={'prefix': '$', 'from': 1, 'to': 10, 'suffix': 'MILLION (AGED 23)', 'roll': [round(t_ten_million + 0.2, 1), round(t_ten_million + 1.2, 1)], 'style': 'paper'},
    job='stat: $10M cash buyout valuation')

# s14: Steve Huffman ringing NYSE Opening Bell
add('video', t_twenty_three, t_ai_dataset, src='clips/reddit_ipo_bell.mp4', **{'from': 0.0},
    push=0.02, dir='L', whip=True,
    job='Steve Huffman ringing NYSE opening bell — $15B public titan')

# s15: Reddit IPO & AI Licensing Deal Card
add('evidence', t_ai_dataset, round(DUR - 3.2, 2), src='img/reddit_ipo_deal_card.png',
    scale=1.55, pos=[350, 140], imgSize=[760, 475], imgOff=[0, 0], dir='R',
    source='NYSE: RDDT · GOOGLE & OPENAI LICENSING DEALS',
    label=[round(t_ai_dataset + 0.3, 1), round(t_ai_dataset + 0.7, 1)],
    job='evidence: Reddit $15.4B IPO and $60M/yr AI dataset deals')

# s16: Pull out to the full 2005 living room photo fading to black
add('still', round(DUR - 3.2, 2), DUR, src='img/yc_2005_class_photo.jpg', fx=0.5, fy=0.5, push=0.02, dir='L',
    job='close: vintage 2005 class photo pull-out fading to black')

# ------------------------------------------------------------------ Automated Multi-Font Editorial Captions
EMPH = {
    'kicked', 'Combinator.', 'phones.', 'Graham', 'dead.', 'internet."',
    'apartment.', '20', 'days.', 'dead.', 'Zero', 'visitors.', 'ghost',
    'profiles.', 'alive.', 'posting.', '16', '10', 'million', 'dollars.',
    '23.', '15', 'billion', 'dollar', 'empire,', 'intelligence.', 'internet.'
}

text = format_caption_chunks(words, EMPH)

annotations = [
    {'t0': 0.8, 't1': 4.8, 'text': 'PRIMARY ARCHIVE · Y COMBINATOR SUMMER 2005', 'pos': 'br'},
    {'t0': round(t_home + 0.2, 1), 't1': round(t_rang - 0.2, 1), 'text': 'PAUL GRAHAM · FOUNDER, Y COMBINATOR', 'pos': 'br'},
    {'t0': round(t_internet_quote + 0.2, 1), 't1': round(t_apartment - 0.2, 1), 'text': 'STEVE HUFFMAN (AGE 21) · CO-FOUNDER, REDDIT', 'pos': 'br'},
    {'t0': round(t_front_page_alive + 0.2, 1), 't1': round(t_posting - 0.2, 1), 'text': 'ALEXIS OHANIAN · CO-FOUNDER, REDDIT', 'pos': 'br'},
    {'t0': round(t_twenty_three + 0.2, 1), 't1': round(t_ai_dataset - 0.2, 1), 'text': 'NEW YORK STOCK EXCHANGE · TICKER: RDDT', 'pos': 'br'},
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
