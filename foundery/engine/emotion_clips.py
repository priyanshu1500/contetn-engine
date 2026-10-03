"""Emotion-tagged relief-clip system (the 'Hollywood integration' from the visual-language review).

Policy (accepted by the user, Option C): relief clips are SPARING and TRANSFORMATIVE —
1-3 seconds each, at most one per 30 seconds of episode runtime, selected by the EMOTION the
beat needs (not by keyword search against the script). `lint.py` enforces the timing/spacing
half of this rule on any shot with `relief: True`; the emotion-matching itself is a judgment
call made when storyboarding, using the table below.

IMPORTANT — sourcing is NOT automatic and NOT pre-downloaded. This file is metadata only: it
records which real, recognizable film moments read as which emotion, so a builder can look one
up when a specific beat needs it. Actually pulling a clip (yt-dlp) happens per-episode, on
request, the same way every other real clip in these episodes was sourced: check the exact
moment, confirm it reads as intended, keep the cut to 1-3s. Do not build a local cache of
pre-ripped movie clips ahead of need.
"""

EMOTION_LIBRARY = {
    'power': [
        {'title': 'House of Cards (Netflix, 2013-2018)', 'note': 'Frank Underwood addressing the camera/a room he controls — use for "consolidating control" beats.'},
    ],
    'collapse': [
        {'title': 'The Big Short (2015)', 'note': 'A trading floor / market-crash montage — use for "the model breaks" beats.'},
    ],
    'control': [
        {'title': 'The Social Network (2010)', 'note': 'A boardroom negotiation or a founder dictating terms — use for "one person reshapes the org" beats.'},
    ],
    'secrecy': [
        {'title': 'Oppenheimer (2023)', 'note': 'A closed-door briefing / classified-document reveal — use for "what wasn\'t said publicly" beats.'},
    ],
    'greed': [
        {'title': 'The Wolf of Wall Street (2013)', 'note': 'A trading-floor frenzy or a sales-pitch monologue — use for "the incentive was always the problem" beats.'},
    ],
}


def pick_relief(emotion: str):
    """Returns the candidate list for an emotion, or [] if none catalogued yet. Extend EMOTION_LIBRARY
    as new emotions/films are validated — don't invent a mapping at build time."""
    return EMOTION_LIBRARY.get(emotion.lower(), [])


def check_relief_shot(shot: dict) -> list[str]:
    """Sanity checks for a single relief shot before it's added to an EDL (lint.py checks timing/spacing
    across the whole episode; this checks the one shot in isolation)."""
    problems = []
    dur = shot['t1'] - shot['t0']
    if not (1.0 <= dur <= 3.0):
        problems.append(f'relief clip duration {dur:.2f}s outside the 1-3s policy')
    if not shot.get('emotion'):
        problems.append('relief shot has no `emotion` tag — pick one from EMOTION_LIBRARY, not a keyword match')
    if not shot.get('source_film'):
        problems.append('relief shot has no `source_film` credit — every relief clip should record what it is')
    return problems
