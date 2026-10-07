import unittest

from duration import parse_duration


class ParseDurationTests(unittest.TestCase):
    def test_valid_cases(self):
        cases = {
            "1h30m": 5400,
            "45s": 45,
            "2h": 7200,
            "1h0m5s": 3605,
            "0h0m0s": 0,
            "10m": 600,
            "5h15s": 5 * 3600 + 15,
        }
        for text, expected in cases.items():
            with self.subTest(text=text):
                self.assertEqual(parse_duration(text), expected)

    def test_invalid_cases(self):
        invalid = ["", "5x", "m5", "30m1h", "1h1h", "1h30m5s10s", "1h30"]
        for text in invalid:
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    parse_duration(text)


if __name__ == "__main__":
    unittest.main()
