import unittest

from roman import to_roman


class ToRomanTest(unittest.TestCase):
    def test_basic_conversions(self):
        cases = {
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            9: "IX",
            10: "X",
            14: "XIV",
            19: "XIX",
            40: "XL",
            44: "XLIV",
            50: "L",
            90: "XC",
            99: "XCIX",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
            1984: "MCMLXXXIV",
            3999: "MMMCMXCIX",
        }
        for number, expected in cases.items():
            with self.subTest(number=number):
                self.assertEqual(to_roman(number), expected)

    def test_invalid_values(self):
        invalid = [0, -1, 4000, 3.5, "X"]
        for value in invalid:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    to_roman(value)


if __name__ == "__main__":
    unittest.main()
