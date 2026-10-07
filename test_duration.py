import unittest

from duration import parse_duration


class ParseDurationTest(unittest.TestCase):
    # Valid cases
    def test_hours_and_minutes(self):
        self.assertEqual(parse_duration("1h30m"), 5400)

    def test_seconds_only(self):
        self.assertEqual(parse_duration("45s"), 45)

    def test_hours_only(self):
        self.assertEqual(parse_duration("2h"), 7200)

    def test_all_components_with_zero(self):
        self.assertEqual(parse_duration("1h0m5s"), 3605)

    # Invalid cases
    def test_empty_string(self):
        with self.assertRaises(ValueError):
            parse_duration("")

    def test_unknown_unit(self):
        with self.assertRaises(ValueError):
            parse_duration("5x")

    def test_missing_number_before_unit(self):
        with self.assertRaises(ValueError):
            parse_duration("m5")

    def test_wrong_order(self):
        with self.assertRaises(ValueError):
            parse_duration("30m1h")

    def test_duplicate_units(self):
        with self.assertRaises(ValueError):
            parse_duration("1h1h")

    def test_extra_characters(self):
        with self.assertRaises(ValueError):
            parse_duration("1h30m30s10s")


if __name__ == "__main__":
    unittest.main()
