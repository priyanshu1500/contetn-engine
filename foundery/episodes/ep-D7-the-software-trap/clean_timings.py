"""
clean_timings.py — Attention Compound Thought-Unit Phrase Grouper for Episode D7.
Groups individual word boundaries into fluid 2-4 word conversational phrases
with centered glowing serif-italic styling (Playfair Display Italic, zero background box).
"""
import json, re

with open('words_timing.json', encoding='utf-8') as f:
    words = json.load(f)

# Punctuation / pause split markers
phrases = []
curr_tokens = []
curr_start = None

# Custom grouping logic to produce natural cinematic thought-units
for i, w in enumerate(words):
    token = w['word'].strip()
    if not token:
        continue
    
    if curr_start is None:
        curr_start = w['start']
        
    curr_tokens.append(token)
    curr_end = w['end']
    
    # Check if phrase should close:
    # 1. Punctuation (., ?, !, :, ...)
    # 2. Token count reached 3-4 words
    # 3. Gap to next word > 0.35s
    gap_to_next = 0.0
    if i < len(words) - 1:
        gap_to_next = round(words[i+1]['start'] - w['end'], 3)
        
    has_punct = any(token.endswith(p) for p in ['.', '?', '!', ':', ';', '...'])
    token_limit = len(curr_tokens) >= 4 or (len(curr_tokens) >= 3 and len(" ".join(curr_tokens)) > 16)
    
    if has_punct or token_limit or gap_to_next > 0.35:
        phrase_text = " ".join(curr_tokens)
        
        # Metric & Entity Normalization
        phrase_text = phrase_text.replace("trillion dollar", "$1 TRILLION")
        phrase_text = phrase_text.replace("fourteen trillion dollars", "$14 TRILLION")
        phrase_text = phrase_text.replace("three point four trillion dollars", "$3.4 TRILLION")
        phrase_text = phrase_text.replace("three hundred and fifty thousand", "350,000")
        
        # Decide styling:
        # High impact metrics use Bebas/gold, narrative uses pure glowing serifItalic
        is_metric = any(sym in phrase_text for sym in ['$', '350,000', '2006'])
        font_kind = "displayCondensed" if is_metric else "serifItalic"
        
        phrases.append({
            "text": phrase_text,
            "start": curr_start,
            "end": curr_end,
            "fontKind": font_kind,
            "box": "none"  # Pure glowing text per Attention Compound standard
        })
        curr_tokens = []
        curr_start = None

# Flush remainder
if curr_tokens:
    phrases.append({
        "text": " ".join(curr_tokens),
        "start": curr_start,
        "end": words[-1]['end'],
        "fontKind": "serifItalic",
        "box": "none"
    })

with open('cleaned_phrases.json', 'w', encoding='utf-8') as f:
    json.dump(phrases, f, indent=2)

print(f"Grouped {len(words)} raw words into {len(phrases)} thought-unit cinematic phrases.")
for p in phrases[:10]:
    print(f"[{p['start']:.2f}s -> {p['end']:.2f}s] ({p['fontKind']}) {p['text']}")

