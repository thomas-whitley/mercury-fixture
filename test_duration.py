import unittest

from duration import parse_duration


class ParseDurationTest(unittest.TestCase):
    def test_hours_and_minutes(self):
        self.assertEqual(parse_duration("1h30m"), 5400)
    
    def test_seconds_only(self):
        self.assertEqual(parse_duration("45s"), 45)
    
    def test_hours_only(self):
        self.assertEqual(parse_duration("2h"), 7200)
    
    def test_all_three_components(self):
        self.assertEqual(parse_duration("1h0m5s"), 3605)
    
    def test_minutes_only(self):
        self.assertEqual(parse_duration("30m"), 1800)
    
    def test_hours_and_seconds(self):
        self.assertEqual(parse_duration("1h5s"), 3605)
    
    def test_minutes_and_seconds(self):
        self.assertEqual(parse_duration("30m5s"), 1805)
    
    def test_zero_hours(self):
        self.assertEqual(parse_duration("0h30m"), 1800)
    
    def test_zero_minutes(self):
        self.assertEqual(parse_duration("1h0m"), 3600)
    
    def test_zero_seconds(self):
        self.assertEqual(parse_duration("1h30m0s"), 5400)
    
    def test_empty_string_raises(self):
        with self.assertRaises(ValueError):
            parse_duration("")
    
    def test_invalid_unit_raises(self):
        with self.assertRaises(ValueError):
            parse_duration("5x")
    
    def test_unit_before_number_raises(self):
        with self.assertRaises(ValueError):
            parse_duration("m5")
    
    def test_wrong_order_raises(self):
        with self.assertRaises(ValueError):
            parse_duration("30m1h")
    
    def test_duplicate_unit_raises(self):
        with self.assertRaises(ValueError):
            parse_duration("1h1h")
    
    def test_spaces_raise(self):
        with self.assertRaises(ValueError):
            parse_duration("1h 30m")
    
    def test_extra_characters_raise(self):
        with self.assertRaises(ValueError):
            parse_duration("1h30m5")
    
    def test_negative_numbers_raise(self):
        with self.assertRaises(ValueError):
            parse_duration("-1h")


if __name__ == "__main__":
    unittest.main()
