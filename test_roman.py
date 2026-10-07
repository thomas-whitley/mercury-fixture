import unittest
from roman import to_roman


class RomanTest(unittest.TestCase):
    def test_basic_conversions(self):
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(3), "III")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(58), "LVIII")
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_out_of_range_raises_value_error(self):
        with self.assertRaises(ValueError):
            to_roman(0)
        with self.assertRaises(ValueError):
            to_roman(4000)
        with self.assertRaises(ValueError):
            to_roman(-1)


if __name__ == "__main__":
    unittest.main()
