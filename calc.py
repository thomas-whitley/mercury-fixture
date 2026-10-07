'''calc module providing simple arithmetic operations.'''

from __future__ import annotations
import sys


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def _print_error(message: str) -> None:
    """Print an error message to stderr."""
    print(message, file=sys.stderr)


def _main(argv: list[str] | None = None) -> int:
    """Entry point for ``python -m calc``.

    Expected usage::

        python -m calc add A B

    Returns exit status 0 on success, 2 on any error.
    """
    if argv is None:
        argv = sys.argv[1:]
    # Expect exactly three arguments: the command "add" and two integers.
    if len(argv) != 3 or argv[0] != "add":
        _print_error("Usage: python -m calc add A B")
        return 2
    _, a_str, b_str = argv
    try:
        a = int(a_str)
        b = int(b_str)
    except ValueError:
        _print_error("A and B must be integers")
        return 2
    result = add(a, b)
    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(_main())
