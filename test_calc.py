import unittest

from calc import add, clamp


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)


class ClampTest(unittest.TestCase):
    def test_clamp_in_range(self):
        self.assertEqual(clamp(5, 1, 10), 5)
    
    def test_clamp_below_range(self):
        self.assertEqual(clamp(0, 1, 10), 1)
    
    def test_clamp_above_range(self):
        self.assertEqual(clamp(15, 1, 10), 10)
    
    def test_clamp_equal_low(self):
        self.assertEqual(clamp(1, 1, 10), 1)
    
    def test_clamp_equal_high(self):
        self.assertEqual(clamp(10, 1, 10), 10)
    
    def test_clamp_invalid_range(self):
        with self.assertRaises(ValueError):
            clamp(5, 10, 1)


if __name__ == "__main__":
    unittest.main()
