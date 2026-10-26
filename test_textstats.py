import unittest

from textstats import word_count


class WordCount(unittest.TestCase):
    def test_single_spaces(self):
        self.assertEqual(word_count("one two three"), 3)

    def test_multiple_spaces(self):
        self.assertEqual(word_count("one   two    three"), 3)

    def test_newlines(self):
        self.assertEqual(word_count("one\ntwo\nthree"), 3)

    def test_tabs(self):
        self.assertEqual(word_count("one\ttwo\tthree"), 3)

    def test_mixed_whitespace(self):
        self.assertEqual(word_count("one  \n\t two   \n three"), 3)

    def test_empty_string(self):
        self.assertEqual(word_count(""), 0)
