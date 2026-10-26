import unittest

from textstats import word_count


class WordCount(unittest.TestCase):
    def test_single_spaces(self):
        self.assertEqual(word_count("one two three"), 3)

    def test_multiple_spaces(self):
        # Multiple spaces between words should be ignored.
        self.assertEqual(word_count("hello   world"), 2)

    def test_newline(self):
        # Newline characters separate words.
        self.assertEqual(word_count("hello\nworld"), 2)

    def test_tab(self):
        # Tab characters separate words.
        self.assertEqual(word_count("hello\tworld"), 2)

    def test_empty_string(self):
        # Empty string should yield a count of 0, not 1.
        self.assertEqual(word_count(""), 0)

    def test_mixed_whitespace(self):
        # Combination of spaces, tabs, and newlines.
        text = "  hello\t\nworld   this is\ta\ttest  "
        self.assertEqual(word_count(text), 6)


if __name__ == "__main__":
    unittest.main()
