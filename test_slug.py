import unittest
from slug import slugify
class TestSlugify(unittest.TestCase):
    def test_slugify(self):
        self.assertEqual(slugify('Hello, World!'), 'hello-world')
        self.assertEqual(slugify(''), '')
if __name__ == '__main__':
    unittest.main()