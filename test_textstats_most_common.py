import pytest
from textstats import most_common


def test_most_common_basic():
    text = "Apple banana apple orange banana apple"
    result = most_common(text, 2)
    assert result == [("apple", 3), ("banana", 2)]


def test_most_common_tie_break_alphabetical():
    text = "cat dog bee bee cat dog"
    # all have count 2, alphabetical order should be bee, cat, dog
    result = most_common(text, 2)
    assert result == [("bee", 2), ("cat", 2)]


def test_most_common_n_greater_than_distinct():
    text = "one two three"
    result = most_common(text, 10)
    # All words appear once, sorted alphabetically because counts tie
    assert result == [("one", 1), ("three", 1), ("two", 1)]


def test_most_common_invalid_n():
    with pytest.raises(ValueError):
        most_common("any text", 0)
    with pytest.raises(ValueError):
        most_common("any text", -5)
