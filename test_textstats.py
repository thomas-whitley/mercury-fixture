import unittest

from textstats import word_count, most_common


class WordCount(unittest.TestCase):
    def test_single_spaces(self):
        self.assertEqual(word_count("one two three"), 3)


class TestMostCommon(unittest.TestCase):
    def test_basic(self):
        text = "apple banana apple orange banana apple"
        result = most_common(text, 2)
        self.assertEqual(result, [("apple", 3), ("banana", 2)])

    def test_tie_alpha(self):
        text = "cat bat dog bat cat dog"
        result = most_common(text, 2)
        # All words appear twice; alphabetical order decides
        self.assertEqual(result, [("bat", 2), ("cat", 2)])

    def test_n_larger_than_distinct(self):
        text = "one two three"
        result = most_common(text, 10)
        # All distinct words, counts are equal (1), alphabetical order decides
        self.assertEqual(result, [("one", 1), ("three", 1), ("two", 1)])

    def test_invalid_n(self):
        with self.assertRaises(ValueError):
            most_common("any text", 0)
