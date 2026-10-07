import unittest

from textstats import word_count, most_common


class WordCount(unittest.TestCase):
    def test_single_spaces(self):
        self.assertEqual(word_count("one two three"), 3)


class MostCommon(unittest.TestCase):
    def test_basic(self):
        text = "apple banana apple orange banana apple"
        self.assertEqual(
            most_common(text, 2),
            [("apple", 3), ("banana", 2)]
        )

    def test_case_insensitive(self):
        text = "Apple APPLE apple banana Banana"
        self.assertEqual(
            most_common(text, 2),
            [("apple", 3), ("banana", 2)]
        )

    def test_tie_breaking(self):
        text = "dog cat bird ant"
        # All counts are 1, should be ordered alphabetically
        self.assertEqual(
            most_common(text, 4),
            [("ant", 1), ("bird", 1), ("cat", 1), ("dog", 1)]
        )

    def test_fewer_than_n(self):
        text = "one two"
        self.assertEqual(
            most_common(text, 5),
            [("one", 1), ("two", 1)]
        )

    def test_invalid_n(self):
        with self.assertRaises(ValueError):
            most_common("hello", 0)
        with self.assertRaises(ValueError):
            most_common("hello", -1)

    def test_empty_text(self):
        self.assertEqual(most_common("   ", 3), [])
