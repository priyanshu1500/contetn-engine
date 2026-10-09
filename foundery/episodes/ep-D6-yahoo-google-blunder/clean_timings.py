"""
clean_timings.py — Typographic and formatting normalization for Episode D6 words_timing.json.
Merges numbers, dollar values, and company entities.
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
    if word.lower() == 'one' and i + 2 < len(words) and words[i+1]['word'].lower() == 'million':
        w['word'] = '$1,000,000'
        if words[i+2]['word'].lower().startswith('dollar'):
            w['end'] = words[i+2]['end']
            skip_count = 2
        else:
            w['end'] = words[i+1]['end']
            skip_count = 1
        cleaned.append(w)
        continue

    # 'three' + 'billion' -> '$3,000,000,000'
    if word.lower() == 'three' and i + 1 < len(words) and words[i+1]['word'].lower().startswith('billion'):
        w['word'] = '$3,000,000,000'
        w['end'] = words[i+1]['end']
        skip_count = 1
        cleaned.append(w)
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

    # 'three' + 'seconds' -> '3 seconds'
    if word.lower() == 'three' and i + 1 < len(words) and words[i+1]['word'].lower().startswith('second'):
        w['word'] = '3 SECONDS'
        w['end'] = words[i+1]['end']
        skip_count = 1
        cleaned.append(w)
        continue

    # 'trillion-dollar' -> '$1 TRILLION'
    if 'trillion' in word.lower():
        w['word'] = '$1 Trillion'

    cleaned.append(w)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(cleaned, f, indent=2)

print(f"[TimingNormalizer] Cleaned words_timing.json down to {len(cleaned)} tokens.")

