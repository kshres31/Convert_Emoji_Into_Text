"""Formatting helpers for emoji statistics."""

from collections import Counter


def format_statistics(counts: Counter[str], descriptions: dict[str, str]) -> str:
    """Return a readable report from emoji counts and descriptions."""
    total = sum(counts.values())
    lines = ["Emoji Statistics", "----------------", f"Total emojis: {total}"]
    if not counts:
        lines.append("No emojis found.")
        return "\n".join(lines)

    for emoji, count in counts.items():
        lines.append(f"{emoji}  {descriptions.get(emoji, 'unknown emoji')}  {count}")
    return "\n".join(lines)
