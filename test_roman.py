import unittest
from roman import to_roman
class TestRoman(unittest.TestCase):
    def test_1_to_5(self):
        self.assertEqual(to_roman(1), 'I')
        self.assertEqual(to_roman(2), 'II')
        self.assertEqual(to_roman(3), 'III')
        self.assertEqual(to_roman(4), 'IV')
        self.assertEqual(to_roman(5), 'V')

    def test_10_to_50(self):
        self.assertEqual(to_roman(10), 'X')
        self.assertEqual(to_roman(20), 'XX')
        self.assertEqual(to_roman(30), 'XXX')
        self.assertEqual(to_roman(40), 'XL')
        self.assertEqual(to_roman(50), 'L')

    def test_100_to_500(self):
        self.assertEqual(to_roman(100), 'C')
        self.assertEqual(to_roman(200), 'CC')
        self.assertEqual(to_roman(300), 'CCC')
        self.assertEqual(to_roman(400), 'CD')
        self.assertEqual(to_roman(500), 'D')

    def test_1000_to_3999(self):
        self.assertEqual(to_roman(1000), 'M')
        self.assertEqual(to_roman(2000), 'MM')
        self.assertEqual(to_roman(3000), 'MMM')
        self.assertEqual(to_roman(3999), 'MMMCMXCIX')

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            to_roman(-1)

    def test_zero_value(self):
        with self.assertRaises(ValueError):
            to_roman(0)

if __name__ == '__main__':
    unittest.main()
