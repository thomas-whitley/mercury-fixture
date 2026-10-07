# Function to convert an integer to a Roman numeral using subtractive notation
def to_roman(n):
    if not (1 <= n <= 3999):
        raise ValueError('Input must be between 1 and 3999')
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
test_roman.py':
# Test suite for the to_roman function
def test_1_to_5():
    assert to_roman(1) == 'I'
    assert to_roman(2) == 'II'
    assert to_roman(3) == 'III'
    assert to_roman(4) == 'IV'
    assert to_roman(5) == 'V'

def test_10_to_50():
    assert to_roman(10) == 'X'
    assert to_roman(20) == 'XX'
    assert to_roman(30) == 'XXX'
    assert to_roman(40) == 'XL'
    assert to_roman(50) == 'L'

def test_100_to_500():
    assert to_roman(100) == 'C'
    assert to_roman(200) == 'CC'
    assert to_roman(300) == 'CCC'
    assert to_roman(400) == 'CD'
    assert to_roman(500) == 'D'

def test_1000_to_3999():
    assert to_roman(1000) == 'M'
    assert to_roman(2000) == 'MM'
    assert to_roman(3000) == 'MMM'
    assert to_roman(3999) == 'MMMCMXCIX'

# Negative and out-of-range tests
def test_negative_numbers():
    try:
        to_roman(-1)
    except ValueError:
        assert True
    else:
        assert False

def test_zero_value():
    try:
        to_roman(0)
    except ValueError:
        assert True
    else:
        assert False

# Run tests
test_1_to_5()
test_10_to_50()
test_100_to_500()
test_1000_to_3999()
test_negative_numbers()
test_zero_value()

print("All tests passed!")