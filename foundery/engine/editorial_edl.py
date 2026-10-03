"""editorial_edl.py — Automated MetroMedia / Editorial Multi-Font Tagging & Shot Builder.

Provides intelligent linguistic entity tagging:
- Numbers, currencies, years -> fontKind='condensed', uppercase
- Emotional/prestige adjectives & verbs -> fontKind='serif-italic'
- Tech entities, companies, metadata -> fontKind='mono'
- Highlight boxes ('yellow' or 'white') on pivotal moments
- Flanking layouts & optical contrast reset slides
"""

import re

# Lexicons for automated multi-font routing
SERIF_ITALIC_TRIGGERS = {
    'dangerous', 'history', 'photograph', 'genius', 'unhinged', 'empire',
    'obsession', 'conviction', 'myth', 'legendary', 'ruthless', 'secret',
    'power', 'insane', 'billion-dollar', 'swarms', 'inversion', 'collapse',
    'titan', 'titans', 'monopoly', 'leverage', 'revolution'
}

MONO_TRIGGERS = {
    'reddit', 'twitch', 'altman', 'cursor', 'openai', 'yc', 'y-combinator',
    'cambridge', 'stanford', 'nvidia', 'jensen', 'huffman', 'sec', 'arr',
    'source', 'classified', 'verified', 'code', 'workers', 'ai'
}

def tag_word(word_str: str, is_em: bool = False):
    """Assigns appropriate typography family, casing, and highlight treatment."""
    clean = re.sub(r'[^\w\$\%\-]', '', word_str).lower()
    raw = word_str
    
    # 1. Numbers / Currencies / Years -> Condensed Heavy
    if re.search(r'\d', clean) or clean.startswith('$') or clean in {'billion', 'million', 'trillion', 'zero'}:
        return {
            'w': raw.upper(),
            'fontKind': 'condensed',
            'em': True,
            'color': '#F7F5EF',
            'box': 'yellow' if ('$' in clean or clean in {'zero', '500', '10000'}) else None,
        }
        
    # 2. Emotional / Dramatic / High-Status words -> Serif Italic (Playfair Display)
    if clean in SERIF_ITALIC_TRIGGERS or is_em:
        return {
            'w': raw,
            'fontKind': 'serif-italic',
            'em': True,
            'color': '#F5C542',
            'rotate': -2 if clean in {'dangerous', 'insane', 'obsession', 'genius'} else 0,
        }
        
    # 3. Technical entities / Brands / Proof -> Monospace
    if clean in MONO_TRIGGERS:
        return {
            'w': raw,
            'fontKind': 'mono',
            'em': True,
            'color': '#F7F5EF',
        }
        
    # 4. Standard conversational baseline -> Clean Sans
    return {
        'w': raw,
        'fontKind': 'sans',
        'em': False,
        'color': '#F7F5EF',
    }

def format_caption_chunks(words_timing, emph_set=None, max_words=3, max_chunk_dur=1.4):
    """Splits timestamped words into kinetic editorial subtitle chunks."""
    emph_set = {e.lower().rstrip('.,!?') for e in (emph_set or set())}
    chunks, cur = [], []
    
    for w in words_timing:
        clean = w['word'].lower().rstrip('.,!?')
        is_em = clean in emph_set or clean in SERIF_ITALIC_TRIGGERS
        cur.append((w, is_em))
        
        # Break chunks on emphasis, punctuation, or chunk length limit
        if len(cur) >= max_words or is_em or w['word'].endswith(('.', '!', '?')):
            chunks.append(cur)
            cur = []
            
    if cur:
        chunks.append(cur)
        
    text_tracks = []
    for i, ch in enumerate(chunks):
        t0 = ch[0][0]['start']
        nxt = chunks[i + 1][0][0]['start'] if i + 1 < len(chunks) else ch[-1][0]['end'] + 0.6
        t1 = min(ch[-1][0]['end'] + 0.22, nxt if nxt - t0 < max_chunk_dur else t0 + max_chunk_dur)
        t1 = min(max(t1, t0 + 0.28), nxt)
        
        chunk_words = []
        for word_dict, is_em in ch:
            tagged = tag_word(word_dict['word'], is_em)
            tagged['t'] = round(word_dict['start'], 3)
            chunk_words.append(tagged)
            
        text_tracks.append({
            't0': round(t0, 3),
            't1': round(t1, 3),
            'mode': 'word',
            'words': chunk_words,
        })
        
    return text_tracks
