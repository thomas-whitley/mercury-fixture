import unittest
from duration import parse_duration


class ParseDurationTest(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(parse_duration("1h30m"), 5400)
        self.assertEqual(parse_duration("45s"), 45)
        self.assertEqual(parse_duration("2h"), 7200)
        self.assertEqual(parse_duration("1h0m5s"), 3605)

    def test_invalid(self):
        invalid_cases = ["", "5x", "m5", "30m1h", "1h1h", "10s5m", "1h30", "h30m"]
        for case in invalid_cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    parse_duration(case)


if __name__ == '__main__':
    unittest.main()
