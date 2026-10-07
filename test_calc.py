import unittest
import subprocess
import sys

from calc import add


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)


class TestCalcCLI(unittest.TestCase):
    """Integration tests for the ``calc`` module's command‑line interface.

    The tests invoke the module with ``python -m calc`` via a subprocess to
    verify correct stdout/stderr handling and exit codes.
    """

    def _run_calc(self, *args: str) -> subprocess.CompletedProcess:
        """Run ``python -m calc`` with the supplied ``args``.

        Returns the ``CompletedProcess`` instance with captured stdout and
        stderr as text.
        """
        cmd = [sys.executable, "-m", "calc", *args]
        return subprocess.run(cmd, capture_output=True, text=True)

    def test_add_success(self) -> None:
        proc = self._run_calc("add", "2", "3")
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(proc.stdout.strip(), "5")
        self.assertEqual(proc.stderr, "")

    def test_missing_argument(self) -> None:
        proc = self._run_calc("add", "2")
        self.assertEqual(proc.returncode, 2)
        self.assertIn("Usage", proc.stderr)

    def test_non_integer_argument(self) -> None:
        proc = self._run_calc("add", "2", "x")
        self.assertEqual(proc.returncode, 2)
        self.assertIn("integers", proc.stderr)

    def test_wrong_command(self) -> None:
        proc = self._run_calc("sub", "2", "3")
        self.assertEqual(proc.returncode, 2)
        self.assertIn("Usage", proc.stderr)


if __name__ == "__main__":
    unittest.main()
