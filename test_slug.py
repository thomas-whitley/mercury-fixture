import unittest

from slug import slugify


class SlugifyTests(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_empty(self):
        self.assertEqual(slugify(""), "")

    def test_multiple_separators(self):
        self.assertEqual(
            slugify("  Multiple   spaces---and***symbols!!!"),
            "multiple-spaces-and-symbols",
        )

    def test_already_slugified(self):
        self.assertEqual(slugify("already-slugified"), "already-slugified")


if __name__ == "__main__":
    unittest.main()
