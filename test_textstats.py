import unittest

from textstats import word_count, most_common


class WordCount(unittest.TestCase):
    def test_single_spaces(self):
        self.assertEqual(word_count("one two three"), 3)


class MostCommon(unittest.TestCase):
    def test_most_common_basic(self):
        text = "apple banana apple orange banana apple"
        result = most_common(text, 2)
        self.assertEqual(result, [("apple", 3), ("banana", 2)])

    def test_most_common_tie_breaker(self):
        text = "cat bat ant cat bat"
        # counts: cat: 2, bat: 2, ant: 1
        # tie between bat and cat -> alphabetically: bat, cat
        result = most_common(text, 2)
        self.assertEqual(result, [("bat", 2), ("cat", 2)])

    def test_case_insensitivity(self):
        text = "Apple APPLE apple Banana"
        result = most_common(text, 2)
        self.assertEqual(result, [("apple", 3), ("banana", 1)])

    def test_fewer_than_n_words(self):
        text = "hello world"
        result = most_common(text, 5)
        self.assertEqual(result, [("hello", 1), ("world", 1)])

    def test_invalid_n(self):
        with self.assertRaises(ValueError):
            most_common("hello", 0)
        with self.assertRaises(ValueError):
            most_common("hello", -1)
