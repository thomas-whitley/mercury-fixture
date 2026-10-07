import unittest

from roman import to_roman

class TestToRoman(unittest.TestCase):
    def test_to_roman(self):
        assert to_roman(1) == 'I'
        assert to_roman(5) == 'V'
        assert to_roman(9) == 'IX'
        assert to_roman(40) == 'XL'
        assert to_roman(90) == 'XC'
        assert to_roman(400) == 'CD'
        assert to_roman(900) == 'CM'
        assert to_roman(3999) == 'MMMCMXCIX'

if __name__ == '__main__':
    unittest.main()