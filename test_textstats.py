import unittest
import pytest
from textstats import word_count


class WordCount(unittest.TestCase):
    def test_single_spaces(self):
        self.assertEqual(word_count("one two three"), 3)


@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("", 0),
        ("   ", 0),
        ("hello", 1),
        ("hello world", 2),
        ("hello   world", 2),
        ("hello\nworld", 2),
        ("hello\tworld", 2),
        ("  hello   world \n new\tline  ", 4),
    ],
)
def test_word_count_whitespace_variations(input_text, expected):
    assert word_count(input_text) == expected
