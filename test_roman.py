import pytest
from roman import to_roman


@pytest.mark.parametrize(
    "number,expected",
    [
        (1, "I"),
        (3, "III"),
        (4, "IV"),
        (5, "V"),
        (9, "IX"),
        (10, "X"),
        (40, "XL"),
        (44, "XLIV"),
        (90, "XC"),
        (99, "XCIX"),
        (400, "CD"),
        (944, "CMXLIV"),
        (1994, "MCMXCIV"),
        (3999, "MMMCMXCIX"),
    ],
)
def test_to_roman_valid(number, expected):
    assert to_roman(number) == expected


@pytest.mark.parametrize(
    "bad_input",
    [0, -1, 4000, 3.5, "X", None],
)
def test_to_roman_invalid(bad_input):
    with pytest.raises(ValueError):
        to_roman(bad_input)
