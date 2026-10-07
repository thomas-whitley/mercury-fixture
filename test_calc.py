import pytest
from calc import clamp


def test_clamp_within_range():
    assert clamp(5, 0, 10) == 5
    assert clamp(0, 0, 10) == 0
    assert clamp(10, 0, 10) == 10


def test_clamp_below_low():
    assert clamp(-5, 0, 10) == 0
    assert clamp(-1, -3, 2) == -1  # already within range


def test_clamp_above_high():
    assert clamp(15, 0, 10) == 10
    assert clamp(3, -2, 2) == 2


def test_clamp_low_greater_than_high():
    with pytest.raises(ValueError):
        clamp(5, 10, 0)
    with pytest.raises(ValueError):
        clamp(5, 3, 2)
