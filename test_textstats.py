import unittest
import pytest

from textstats import word_count, most_common


class WordCount(unittest.TestCase):
    def test_single_spaces(self):
        self.assertEqual(word_count("one two three"), 3)


def test_most_common_basic():
    text = "Apple banana apple orange banana apple"
    # apple:3, banana:2, orange:1
    expected = [("apple", 3), ("banana", 2)]
    assert most_common(text, 2) == expected


def test_most_common_tie_break_alphabetical():
    text = "cat dog bird dog cat bird"
    # cat:2, dog:2, bird:2 -> alphabetical order
    expected = [("bird", 2), ("cat", 2), ("dog", 2)]
    assert most_common(text, 3) == expected


def test_most_common_n_larger_than_distinct():
    text = "one two three"
    expected = [("one", 1), ("three", 1), ("two", 1)]
    # request more items than distinct words
    assert most_common(text, 10) == expected


def test_most_common_invalid_n():
    with pytest.raises(ValueError):
        most_common("some text", 0)
    with pytest.raises(ValueError):
        most_common("some text", -5)
