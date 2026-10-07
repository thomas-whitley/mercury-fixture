import unittest

from roman import to_roman


class ToRomanTest(unittest.TestCase):
    def test_basic_numbers(self):
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(58), "LVIII")  # L + V + III
        self.assertEqual(to_roman(1994), "MCMXCIV")

    def test_bounds(self):
        self.assertEqual(to_roman(3999), "MMMCMXCIX")
        with self.assertRaises(ValueError):
            to_roman(0)
        with self.assertRaises(ValueError):
            to_roman(4000)
        with self.assertRaises(ValueError):
            to_roman(-5)


if __name__ == "__main__":
    unittest.main()
