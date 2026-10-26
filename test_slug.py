import unittest
from slug import slugify


class TestSlugify(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_empty(self):
        self.assertEqual(slugify(""), "")

    def test_multiple_non_alnum(self):
        self.assertEqual(slugify("Python---Rocks!!"), "python-rocks")

    def test_leading_trailing_hyphens(self):
        self.assertEqual(slugify("--Hello--"), "hello")

    def test_non_ascii(self):
        # Characters like é, ü are not ASCII letters, so they become hyphens
        self.assertEqual(slugify("Café Münster"), "caf-m-nster")


if __name__ == "__main__":
    unittest.main()
