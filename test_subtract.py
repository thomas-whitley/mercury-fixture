import unittest

from calc import subtract


class SubtractTest(unittest.TestCase):
    def test_subtracts_the_second_from_the_first(self):
        self.assertEqual(subtract(5, 3), 2)
