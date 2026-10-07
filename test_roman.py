import unittest
from roman import to_roman


class RomanTest(unittest.TestCase):
    def test_examples(self):
        cases = [
            (1, "I"),
            (4, "IV"),
            (9, "IX"),
            (58, "LVIII"),
            (1994, "MCMXCIV"),
            (3999, "MMMCMXCIX"),
        ]
        for num, expected in cases:
            with self.subTest(num=num):
                self.assertEqual(to_roman(num), expected)

    def test_invalid(self):
        for invalid in (0, -5, 4000, 5000):
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    to_roman(invalid)


if __name__ == "__main__":
    unittest.main()
