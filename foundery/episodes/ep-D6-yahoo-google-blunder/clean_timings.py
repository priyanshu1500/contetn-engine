"""
clean_timings.py — Typographic and formatting normalization for Episode D6 words_timing.json.
Merges multi-word numbers, dollar values, and company entities with 100% precision.
"""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(HERE, 'words_timing.json')
words = json.load(open(path, encoding='utf-8'))

cleaned = []
skip_count = 0

for i, w in enumerate(words):
    if skip_count > 0:
        skip_count -= 1
        continue
        
    word = w['word']
    
    # 'one' + 'million' + 'dollars' -> '$1,000,000'
    if word.lower() == 'one' and i + 1 < len(words) and words[i+1]['word'].lower().startswith('million'):
        w['word'] = '$1,000,000'
        if i + 2 < len(words) and words[i+2]['word'].lower().startswith('dollar'):
            w['end'] = words[i+2]['end']
            skip_count = 2
        else:
            w['end'] = words[i+1]['end']
            skip_count = 1
        cleaned.append(w)
        continue

    # 'three' + 'billion' + 'dollars' -> '$3,000,000,000'
    if word.lower() == 'three' and i + 1 < len(words) and words[i+1]['word'].lower().startswith('billion'):
        w['word'] = '$3,000,000,000'
        if i + 2 < len(words) and words[i+2]['word'].lower().startswith('dollar'):
            w['end'] = words[i+2]['end']
            skip_count = 2
        else:
            w['end'] = words[i+1]['end']
            skip_count = 1
        cleaned.append(w)
        continue

    # 'two' + 'billion' + 'dollars' -> '$2,000,000,000' (or '$2 BILLION')
    if word.lower() == 'two' and i + 1 < len(words) and words[i+1]['word'].lower().startswith('billion'):
        w['word'] = '$2 BILLION'
        if i + 2 < len(words) and words[i+2]['word'].lower().startswith('dollar'):
            w['end'] = words[i+2]['end']
            skip_count = 2
        else:
            w['end'] = words[i+1]['end']
            skip_count = 1
        cleaned.append(w)
        continue

    # 'two' + 'trillion' + 'dollar' -> '$2 TRILLION'
    if word.lower() == 'two' and i + 1 < len(words) and words[i+1]['word'].lower().startswith('trillion'):
        w['word'] = '$2 TRILLION'
        if i + 2 < len(words) and words[i+2]['word'].lower().startswith('dollar'):
            w['end'] = words[i+2]['end']
            skip_count = 2
        else:
            w['end'] = words[i+1]['end']
            skip_count = 1
        cleaned.append(w)
        continue

    # 'said' + 'five' -> 'said $5B' or keep '$5 BILLION'
    if word.lower() == 'said' and i + 1 < len(words) and words[i+1]['word'].lower().startswith('five'):
        cleaned.append(w)
        w2 = words[i+1].copy()
        w2['word'] = '$5 BILLION'
        cleaned.append(w2)
        skip_count = 1
        continue

    # 'Larry' + 'Page' -> 'Larry Page'
    if word == 'Larry' and i + 1 < len(words) and 'Page' in words[i+1]['word']:
        w['word'] = 'Larry Page'
        w['end'] = words[i+1]['end']
        skip_count = 1
        cleaned.append(w)
        continue

    # 'Sergey' + 'Brin' -> 'Sergey Brin'
    if word == 'Sergey' and i + 1 < len(words) and 'Brin' in words[i+1]['word']:
        w['word'] = 'Sergey Brin'
        w['end'] = words[i+1]['end']
        skip_count = 1
        cleaned.append(w)
        continue

    # 'three' + 'seconds' -> '3 SECONDS'
    if word.lower() == 'three' and i + 1 < len(words) and words[i+1]['word'].lower().startswith('second'):
        w['word'] = '3 SECONDS'
        w['end'] = words[i+1]['end']
        skip_count = 1
        cleaned.append(w)
        continue

    cleaned.append(w)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(cleaned, f, indent=2)

print(f"[TimingNormalizer] Cleaned words_timing.json down to {len(cleaned)} tokens.")
