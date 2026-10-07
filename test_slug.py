import unittest

from slug import slugify


class SlugifyTest(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_empty(self):
        self.assertEqual(slugify(""), "")

    def test_special_characters(self):
        self.assertEqual(slugify("---foo   bar---"), "foo-bar")
        self.assertEqual(slugify("Python 3.10 is here!"), "python-3-10-is-here")
