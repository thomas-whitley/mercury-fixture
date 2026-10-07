import unittest

from textstats import word_count


class WordCount(unittest.TestCase):
    def test_single_spaces(self):
        self.assertEqual(word_count("one two three"), 3)

    def test_multiple_spaces(self):
        self.assertEqual(word_count("one  two   three"), 3)

    def test_newlines_and_tabs(self):
        self.assertEqual(word_count("one\ntwo\tthree"), 3)

    def test_empty_string(self):
        self.assertEqual(word_count(""), 0)

    def test_whitespace_only(self):
        self.assertEqual(word_count("   \n\t "), 0)
