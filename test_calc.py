import unittest
import subprocess
import sys

from calc import add


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)


class CalcCLItest(unittest.TestCase):
    def _run(self, *cmd):
        """Run ``python -m calc`` with the given arguments and capture output."""
        return subprocess.run(
            [sys.executable, "-m", "calc"] + list(cmd),
            capture_output=True,
            text=True,
        )

    def test_cli_success(self):
        result = self._run("add", "2", "3")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "5")
        self.assertEqual(result.stderr, "")

    def test_cli_invalid_command(self):
        result = self._run("sub", "2", "3")
        self.assertEqual(result.returncode, 2)
        self.assertTrue(result.stderr.strip())

    def test_cli_missing_argument(self):
        result = self._run("add", "2")
        self.assertEqual(result.returncode, 2)
        self.assertTrue(result.stderr.strip())

    def test_cli_non_integer(self):
        result = self._run("add", "2", "x")
        self.assertEqual(result.returncode, 2)
        self.assertTrue(result.stderr.strip())


if __name__ == "__main__":
    unittest.main()
