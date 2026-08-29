"""Core text conversion helpers for the Emoji Text Converter."""

from collections import Counter
from typing import List, Tuple

import demoji

EmojiMatch = Tuple[str, str]


def detect_emojis(text: str) -> List[EmojiMatch]:
    """Return emojis and their descriptions in the order they appear."""
    descriptions = demoji.findall(text)
    matches = []
    position = 0
    while position < len(text):
        found = next((emoji for emoji in descriptions if text.startswith(emoji, position)), None)
        if found is None:
            position += 1
            continue
        matches.append((found, descriptions[found]))
        position += len(found)
    return matches


def remove_emojis(text: str) -> str:
    """Remove emojis while preserving the surrounding text."""
    return demoji.replace(text, "")


def replace_emojis(text: str) -> str:
    """Replace each emoji with its readable name surrounded by colons."""
    return demoji.replace_with_desc(text, sep=":")


def get_emoji_statistics(text: str) -> Counter[str]:
    """Count each distinct emoji found in text."""
    return Counter(emoji for emoji, _ in detect_emojis(text))
