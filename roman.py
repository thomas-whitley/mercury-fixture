def to_roman(n):
    if not isinstance(n, int) or not (1 <= n <= 3999):
        raise ValueError('Input must be an integer between 1 and 3999')
    val = (
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    )
    result = ''
    for (arabic, roman) in val:
        while n >= arabic:
            result += roman
            n -= arabic
    return result
