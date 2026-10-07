import unittest

from textstats import word_count, most_common


class WordCount(unittest.TestCase):
    def test_single_spaces(self):
        self.assertEqual(word_count('one two three'), 3)


class MostCommon(unittest.TestCase):
    def test_basic(self):
        text = 'apple banana Apple banana orange apple'
        # apple:3, banana:2, orange:1
        self.assertEqual(most_common(text, 2), [('apple', 3), ('banana', 2)])

    def test_tie_break(self):
        text = 'cat bat dog bat cat dog'
        # each word appears twice; alphabetical tie‑break
        self.assertEqual(most_common(text, 3), [('bat', 2), ('cat', 2), ('dog', 2)])

    def test_n_larger_than_distinct(self):
        text = 'one two three'
        # all counts are 1; alphabetical order
        self.assertEqual(most_common(text, 5), [('one', 1), ('three', 1), ('two', 1)])

    def test_invalid_n(self):
        with self.assertRaises(ValueError):
            most_common('test', 0)
