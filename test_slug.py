import pytest
from slug import slugify

@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("Hello, World!", "hello-world"),
        ("", ""),
        ("   Multiple   Spaces   ", "multiple-spaces"),
        ("---Leading and trailing---", "leading-and-trailing"),
        ("Café au lait", "c-af-au-lait"),  # non‑ASCII characters become separators
    ],
)
def test_slugify(input_text, expected):
    assert slugify(input_text) == expected
