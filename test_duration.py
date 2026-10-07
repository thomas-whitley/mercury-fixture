import unittest

from duration import parse_duration


class DurationTest(unittest.TestCase):
    def test_valid_durations(self):
        self.assertEqual(parse_duration("1h30m"), 5400)
        self.assertEqual(parse_duration("45s"), 45)
        self.assertEqual(parse_duration("2h"), 7200)
        self.assertEqual(parse_duration("1h0m5s"), 3605)
        self.assertEqual(parse_duration("30m"), 1800)
        self.assertEqual(parse_duration("1h2m3s"), 3723)

    def test_invalid_durations(self):
        invalid_inputs = [
            "",
            "5x",
            "m5",
            "30m1h",
            "1h1h",
            "1s2h",
            "h",
            "1.5h",
            "-1h",
            " 1h",
            "1h ",
        ]
        for text in invalid_inputs:
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    parse_duration(text)


if __name__ == "__main__":
    unittest.main()
