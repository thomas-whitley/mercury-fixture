import unittest
import subprocess
import sys

from calc import add


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)


class CLITest(unittest.TestCase):
    def _run(self, *extra_args):
        return subprocess.run(
            [sys.executable, "-m", "calc"] + list(extra_args),
            capture_output=True,
            text=True,
        )

    def test_cli_success(self):
        result = self._run("add", "2", "3")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "5")
        self.assertEqual(result.stderr, "")

    def test_cli_missing_arguments(self):
        result = self._run("add", "2")
        self.assertEqual(result.returncode, 2)
        self.assertNotEqual(result.stderr.strip(), "")

    def test_cli_non_integer_argument(self):
        result = self._run("add", "x", "1")
        self.assertEqual(result.returncode, 2)
        self.assertNotEqual(result.stderr.strip(), "")

    def test_cli_wrong_command(self):
        result = self._run("subtract", "2", "3")
        self.assertEqual(result.returncode, 2)
        self.assertNotEqual(result.stderr.strip(), "")


if __name__ == "__main__":
    unittest.main()
