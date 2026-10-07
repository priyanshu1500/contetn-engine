"""
clean_timings.py — Typographic and formatting normalization for Episode D5 words_timing.json.
Merges split numbers and proper nouns (e.g. 'twenty' + 'ten' -> '2010', 'Palo' + 'Alto' -> 'Palo Alto').
"""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(HERE, 'words_timing.json')
words = json.load(open(path, encoding='utf-8'))

cleaned = []
skip_next = False

for i, w in enumerate(words):
    if skip_next:
        skip_next = False
        continue
        
    word = w['word']
    
    # Merge 'twenty' + 'ten' -> '2010,'
    if word.lower() == 'twenty' and i + 1 < len(words) and words[i+1]['word'].lower().startswith('ten'):
        w['word'] = '2010,'
        w['end'] = words[i+1]['end']
        skip_next = True
        cleaned.append(w)
        continue

    # 'Palo' + 'Alto'
    if word == 'Palo' and i + 1 < len(words) and 'Alto' in words[i+1]['word']:
        w['word'] = 'Palo Alto'
        w['end'] = words[i+1]['end']
        skip_next = True
        cleaned.append(w)
        continue

    # 'Silicon' + 'Valley'
    if word == 'Silicon' and i + 1 < len(words) and 'Valley' in words[i+1]['word']:
        w['word'] = 'Silicon Valley.'
        w['end'] = words[i+1]['end']
        skip_next = True
        cleaned.append(w)
        continue
        
    # 'Collison' + 'Installation'
    if word == 'Collison' and i + 1 < len(words) and 'Installation' in words[i+1]['word']:
        w['word'] = 'Collison Installation.'
        w['end'] = words[i+1]['end']
        skip_next = True
        cleaned.append(w)
        continue

    # 'one' + 'trillion' -> '$1 Trillion'
    if word.lower() == 'one' and i + 1 < len(words) and words[i+1]['word'].lower().startswith('trillion'):
        w['word'] = '$1 Trillion'
        w['end'] = words[i+1]['end']
        skip_next = True
        cleaned.append(w)
        continue
        
    cleaned.append(w)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(cleaned, f, indent=2)

print('Cleaned words_timing.json saved! Word count:', len(cleaned))
