import unittest

from textstats import word_count


class WordCount(unittest.TestCase):
    def test_single_spaces(self):
        self.assertEqual(word_count("one two three"), 3)

    def test_multiple_spaces(self):
        self.assertEqual(word_count("hello   world"), 2)

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(word_count("  leading and trailing  "), 3)

    def test_newline_and_tab(self):
        self.assertEqual(word_count("hello\nworld"), 2)
        self.assertEqual(word_count("hello\tworld"), 2)
        self.assertEqual(word_count("multiple\n\tseparators"), 2)

    def test_empty_string(self):
        self.assertEqual(word_count(""), 0)

    def test_mixed_whitespace(self):
        text = '  hello\t\n  world  \n\tpython  '
        self.assertEqual(word_count(text), 3)
