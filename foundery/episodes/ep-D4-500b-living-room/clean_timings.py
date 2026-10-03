import json

path = r'D:\agency content\BIN\documentary_tofu\ep-D4-500b-living-room\words_timing.json'
words = json.load(open(path, encoding='utf-8'))

cleaned = []

for i, w in enumerate(words):
    raw = w['word']
    
    # 222 -year -old -> 'two 22-year-old'
    if raw == '222':
        w['word'] = 'two 22-year-old'
        cleaned.append(w)
        continue
    if raw in ['-year', '-old']:
        continue
        
    if raw == 'Graham.' and i == 47:
        w['word'] = 'Graham:'
    elif raw == 'Your' and i == 48:
        w['word'] = '"Your'
    elif raw == 'internet.' and i == 62:
        w['word'] = 'internet."'
    elif 'Achanian' in raw or 'Ahenian' in raw:
        w['word'] = 'Ohanian'
    elif raw == 'uploaded':
        w['word'] = 'upvoted'
    elif 'Cond' in raw:
        w['word'] = 'Condé'
    elif raw == 'million.' and i == 164:
        w['word'] = 'million dollars.'
    elif raw == 'billion' and i == 173:
        w['word'] = 'billion dollar'
        
    cleaned.append(w)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(cleaned, f, indent=2)

print('Cleaned words saved! Total words:', len(cleaned))
for idx in [2, 3, 4, 11, 12, 43, 44, 45, 46, 58, 59, 60, 61, 62, 63, 64, 120, 121, 122, 150, 151, 152, 166, 167]:
    if idx < len(cleaned):
        print(f'{idx}: {cleaned[idx]["word"]}')

