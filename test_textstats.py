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

    def test_case_insensitivity(self):
        text = "Apple APPLE apple Banana banana"
        self.assertEqual(
            most_common(text, 1),
            [("apple", 3)]
        )

    def test_tie_breaking(self):
        text = "cat dog bird cat dog"
        # Counts: cat: 2, dog: 2, bird: 1
        # Ties between cat and dog should be resolved alphabetically: cat, then dog
        self.assertEqual(
            most_common(text, 3),
            [("cat", 2), ("dog", 2), ("bird", 1)]
        )

    def test_fewer_than_n(self):
        text = "one two"
        self.assertEqual(
            most_common(text, 5),
            [("one", 1), ("two", 1)]
        )

    def test_invalid_n(self):
        with self.assertRaises(ValueError):
            most_common("some text", 0)
        with self.assertRaises(ValueError):
            most_common("some text", -1)
