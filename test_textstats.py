import unittest

from textstats import word_count, most_common


class WordCount(unittest.TestCase):
    def test_single_spaces(self):
        self.assertEqual(word_count("one two three"), 3)


class MostCommon(unittest.TestCase):
    def test_basic_most_common(self):
        text = "apple banana apple orange banana apple"
        # counts: apple: 3, banana: 2, orange: 1
        self.assertEqual(
            most_common(text, 2),
            [("apple", 3), ("banana", 2)]
        )

    def test_case_insensitivity(self):
        text = "Apple APPLE apple Banana banana"
        # lowercased: apple: 3, banana: 2
        self.assertEqual(
            most_common(text, 5),
            [("apple", 3), ("banana", 2)]
        )

    def test_tie_breaking_alphabetical(self):
        text = "dog cat bat dog cat bat"
        # counts: bat: 2, cat: 2, dog: 2
        # alphabetical tie-break: bat, cat, dog
        self.assertEqual(
            most_common(text, 3),
            [("bat", 2), ("cat", 2), ("dog", 2)]
        )

    def test_fewer_than_n_words(self):
        text = "hello world"
        self.assertEqual(
            most_common(text, 5),
            [("hello", 1), ("world", 1)]
        )

    def test_invalid_n_raises_value_error(self):
        with self.assertRaises(ValueError):
            most_common("hello", 0)
        with self.assertRaises(ValueError):
            most_common("hello", -1)
