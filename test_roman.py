import unittest

from roman import to_roman


class RomanTest(unittest.TestCase):
    def test_single_digits(self):
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(5), "V")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(10), "X")

    def test_subtractive_notation(self):
        self.assertEqual(to_roman(40), "XL")
        self.assertEqual(to_roman(90), "XC")
        self.assertEqual(to_roman(400), "CD")
        self.assertEqual(to_roman(900), "CM")

    def test_complex_numbers(self):
        self.assertEqual(to_roman(58), "LVIII")   # 50 + 5 + 3
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_invalid_values(self):
        for invalid in [0, -1, 4000, 5000]:
            with self.subTest(invalid=invalid):
                self.assertRaises(ValueError, to_roman, invalid)


if __name__ == "__main__":
    unittest.main()
