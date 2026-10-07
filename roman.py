'''roman.py
Provides conversion from integer to Roman numeral using subtractive notation.
'''

from typing import List, Tuple


def to_roman(n: int) -> str:
    """Return the Roman numeral representation of ``n``.

    Args:
        n: An integer between 1 and 3999 inclusive.

    Returns:
        A string containing the Roman numeral.

    Raises:
        ValueError: If ``n`` is not an int or is outside the allowed range.
    """
    if not isinstance(n, int):
        raise ValueError("Roman numerals can only be generated from integers")
    if n < 1 or n > 3999:
        raise ValueError("Integer out of range (must be 1..3999)")

    # Mapping of integer values to Roman numerals, ordered from largest to smallest.
    roman_map: List[Tuple[int, str]] = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result = []
    remainder = n
    for value, numeral in roman_map:
        count, remainder = divmod(remainder, value)
        result.append(numeral * count)
        if remainder == 0:
            break
    return "".join(result)
