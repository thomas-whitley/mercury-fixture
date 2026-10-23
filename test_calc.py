import unittest

from calc import add, clamp


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)


class ClampTest(unittest.TestCase):
    def test_clamp_below(self):
        self.assertEqual(clamp(1, 2, 10), 2)

    def test_clamp_above(self):
        self.assertEqual(clamp(15, 2, 10), 10)

    def test_clamp_normal(self):
        self.assertEqual(clamp(5, 2, 10), 5)

    def test_clamp_equal(self):
        self.assertEqual(clamp(2, 2, 10), 2)
        self.assertEqual(clamp(10, 2, 10), 10)

    def test_clamp_invalid_range(self):
        with self.assertRaises(ValueError):
            clamp(5, 10, 2)


if __name__ == "__main__":
    unittest.main()
