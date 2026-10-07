def to_roman(n: int) -> str:
    """Convert an integer to a Roman numeral.

    Args:
        n: Integer between 1 and 3999 inclusive.

    Returns:
        A string representing the Roman numeral.

    Raises:
        ValueError: If ``n`` is not within the valid range.
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 1 or n > 3999:
        raise ValueError("Roman numerals only support numbers from 1 to 3999")

    # Mapping of integer values to Roman numerals in descending order.
    roman_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]

    result = []
    remaining = n
    for value, numeral in roman_map:
        count, remaining = divmod(remaining, value)
        result.append(numeral * count)
        if remaining == 0:
            break
    return "".join(result)
