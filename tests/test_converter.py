import unittest

from src.converter import detect_emojis, get_emoji_statistics, remove_emojis, replace_emojis


class ConverterTests(unittest.TestCase):
    def test_detects_multiple_emojis(self):
        self.assertEqual([emoji for emoji, _ in detect_emojis("Python 🐍 is fun! 🔥")], ["🐍", "🔥"])

    def test_text_without_emojis(self):
        self.assertEqual(detect_emojis("Plain text"), [])
        self.assertEqual(get_emoji_statistics("Plain text"), {})

    def test_removes_emojis(self):
        self.assertEqual(remove_emojis("Hello 🎉 world!"), "Hello  world!")

    def test_replaces_emojis(self):
        self.assertEqual(replace_emojis("I code 💻"), "I code :laptop:")

    def test_counts_repeated_emojis(self):
        self.assertEqual(get_emoji_statistics("🐍🐍🔥"), {"🐍": 2, "🔥": 1})

    def test_empty_text(self):
        self.assertEqual(detect_emojis(""), [])
        self.assertEqual(remove_emojis(""), "")
        self.assertEqual(replace_emojis(""), "")


if __name__ == "__main__":
    unittest.main()
