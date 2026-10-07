import unittest

from slug import slugify


class SlugifyTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_empty(self):
        self.assertEqual(slugify(""), "")

    def test_special_characters(self):
        self.assertEqual(slugify("   Foo  Bar---Baz... "), "foo-bar-baz")

    def test_digits_and_letters(self):
        self.assertEqual(slugify("Item 123 Price $10.99"), "item-123-price-10-99")


if __name__ == "__main__":
    unittest.main()
