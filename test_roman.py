import unittest
from roman import to_roman


class RomanTest(unittest.TestCase):
    def test_basic_conversions(self):
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(3), "III")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(5), "V")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(10), "X")
        self.assertEqual(to_roman(40), "XL")
        self.assertEqual(to_roman(50), "L")
        self.assertEqual(to_roman(90), "XC")
        self.assertEqual(to_roman(100), "C")
        self.assertEqual(to_roman(400), "CD")
        self.assertEqual(to_roman(500), "D")
        self.assertEqual(to_roman(900), "CM")
        self.assertEqual(to_roman(1000), "M")

    def test_complex_conversions(self):
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            to_roman(0)
        with self.assertRaises(ValueError):
            to_roman(4000)
        with self.assertRaises(ValueError):
            to_roman(-5)


if __name__ == "__main__":
    unittest.main()
