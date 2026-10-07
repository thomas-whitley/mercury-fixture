import unittest

from duration import parse_duration


class ParseDurationTest(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(parse_duration("1h30m"), 5400)
        self.assertEqual(parse_duration("45s"), 45)
        self.assertEqual(parse_duration("2h"), 7200)
        self.assertEqual(parse_duration("1h0m5s"), 3605)
        self.assertEqual(parse_duration("0s"), 0)
        self.assertEqual(parse_duration("0h0m"), 0)

    def test_invalid(self):
        for bad in ["", "5x", "m5", "30m1h", "1h1h", "h5", "1h30m5h"]:
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    parse_duration(bad)


if __name__ == "__main__":
    unittest.main()
