import unittest

from textstats import word_count


class WordCount(unittest.TestCase):
    def test_single_spaces(self):
        self.assertEqual(word_count("one two three"), 3)

    def test_empty_string(self):
        self.assertEqual(word_count(""), 0)
        self.assertEqual(word_count("   "), 0)

    def test_multiple_spaces_newlines_tabs(self):
        self.assertEqual(word_count("one  two   three"), 3)
        self.assertEqual(word_count("one\ntwo\nthree"), 3)
        self.assertEqual(word_count("one\ttwo\tthree"), 3)
        self.assertEqual(word_count("one \n\t two  three"), 3)
