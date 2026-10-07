import unittest
from duration import parse_duration

class TestParseDuration(unittest.TestCase):
    def test_h(self):
        self.assertEqual(parse_duration('2h'), 7200)
    def test_m(self):
        self.assertEqual(parse_duration('30m'), 1800)
    def test_s(self):
        self.assertEqual(parse_duration('45s'), 45)
    def test_hms(self):
        self.assertEqual(parse_duration('1h:0m:5s'), 3605)
    def test_invalid(self):
        with self.assertRaises(ValueError):
            parse_duration('')
        with self.assertRaises(ValueError):
            parse_duration('5x')
        with self.assertRaises(ValueError):
            parse_duration('m5')
        with self.assertRaises(ValueError):
            parse_duration('30m1h')
        with self.assertRaises(ValueError):
            parse_duration('1h1h')
if __name__ == '__main__':
    unittest.main()
