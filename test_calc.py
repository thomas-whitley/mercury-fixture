import unittest
import subprocess
import sys

from calc import add


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_cli_add(self):
        res = subprocess.run(
            [sys.executable, "-m", "calc", "add", "2", "3"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(res.returncode, 0)
        self.assertEqual(res.stdout, "5\n")
        self.assertEqual(res.stderr, "")

    def test_cli_invalid_args_count(self):
        res = subprocess.run(
            [sys.executable, "-m", "calc", "add", "2"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(res.returncode, 2)
        self.assertNotEqual(res.stderr, "")

    def test_cli_invalid_int(self):
        res = subprocess.run(
            [sys.executable, "-m", "calc", "add", "a", "3"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(res.returncode, 2)
        self.assertNotEqual(res.stderr, "")

    def test_cli_invalid_command(self):
        res = subprocess.run(
            [sys.executable, "-m", "calc", "sub", "2", "3"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(res.returncode, 2)
        self.assertNotEqual(res.stderr, "")


if __name__ == "__main__":
    unittest.main()
