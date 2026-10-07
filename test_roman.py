import pytest
from roman import to_roman

@pytest.mark.parametrize(
    "num,expected",
    [
        (1, "I"),
        (4, "IV"),
        (9, "IX"),
        (58, "LVIII"),  # 50 + 5 + 3
        (1994, "MCMXCIV"),
        (3999, "MMMCMXCIX"),
    ],
)
def test_to_roman_valid(num, expected):
    assert to_roman(num) == expected


def test_to_roman_invalid():
    for invalid in [0, -1, 4000, 5000, None, "X"]:
        with pytest.raises(ValueError):
            to_roman(invalid)
