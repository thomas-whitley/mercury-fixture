import unittest

from roman import to_roman

class TestRoman(unittest.TestCase):
    def test_valid_numbers(self):
        self.assertEqual(to_roman(1), 'I')
        self.assertEqual(to_roman(4), 'IV')
        self.assertEqual(to_roman(5), 'V')
        self.assertEqual(to_roman(9), 'IX')
        self.assertEqual(to_roman(10), 'X')
        self.assertEqual(to_roman(40), 'XL')
        self.assertEqual(to_roman(90), 'XC')
        self.assertEqual(to_roman(100), 'C')
        self.assertEqual(to_roman(400), 'CD')
        self.assertEqual(to_roman(900), 'CM')
        self.assertEqual(to_roman(3999), 'MMMCMXCIX')
if __name__ == '__main__':
    unittest.main()