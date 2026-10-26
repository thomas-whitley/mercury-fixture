import pytest
from duration import parse_duration


@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("1h30m", 5400),
        ("45s", 45),
        ("2h", 7200),
        ("1h0m5s", 3605),
        ("0h0m0s", 0),
        ("10m", 600),
        ("5h5s", 18005),
    ],
)
def test_parse_duration_valid(input_text, expected):
    assert parse_duration(input_text) == expected


@pytest.mark.parametrize(
    "input_text",
    [
        "",
        "5x",
        "m5",
        "30m1h",
        "1h1h",
        "1h30m5s6",
        "h",
        "1h30",
        "1 h30m",
    ],
)
def test_parse_duration_invalid(input_text):
    with pytest.raises(ValueError):
        parse_duration(input_text)
