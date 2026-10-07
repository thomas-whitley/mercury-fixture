import unittest

from slug import slugify

class TestSlug(unittest.TestCase):
    def test_hello_space_world(self):
        self.assertEqual(slugify("Hello, World!") , "hello-world")
    def test_empty(self):
        self.assertEqual(slugify("") , "")
    def test_repeated_punctuation(self):
        self.assertEqual(slugify("aaaa,,bbbbb") , "aaaa-bbbbb")
    def test_leading_trailing_spaces(self):
        self.assertEqual(slugify("  hello  ") , "hello")
if __name__ == "__main__":
    unittest.main()