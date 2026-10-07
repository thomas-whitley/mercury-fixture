import unittest
import pytest
from textstats import word_count, most_common


class WordCount(unittest.TestCase):
    def test_single_spaces(self):
        self.assertEqual(word_count("one two three"), 3)


# pytest style tests for most_common

def test_most_common_basic():
    text = "Apple banana apple orange banana apple"
    result = most_common(text, 2)
    assert result == [("apple", 3), ("banana", 2)]


def test_most_common_tie_break_alphabetical():
    text = "cat dog bee bee cat dog"
    result = most_common(text, 2)
    assert result == [("bee", 2), ("cat", 2)]


def test_most_common_n_greater_than_distinct():
    text = "one two three"
    result = most_common(text, 10)
    assert result == [("one", 1), ("three", 1), ("two", 1)]


def test_most_common_invalid_n():
    with pytest.raises(ValueError):
        most_common("any text", 0)
    with pytest.raises(ValueError):
        most_common("any text", -5)
