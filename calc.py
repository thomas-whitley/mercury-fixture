'''A deliberately small module for Mercury's repo chore integration test to edit.'''

import sys


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def _cli() -> None:
    """Command‑line interface for ``python -m calc``.

    Expected usage:
        python -m calc add A B
    where ``A`` and ``B`` are integers.
    On success prints the sum and exits with status 0.
    Any other usage prints an error message to stderr and exits with status 2.
    """
    args = sys.argv[1:]
    if len(args) != 3 or args[0] != "add":
        print("Invalid arguments", file=sys.stderr)
        sys.exit(2)
    _, a_str, b_str = args
    try:
        a = int(a_str)
        b = int(b_str)
    except ValueError:
        print("Invalid arguments", file=sys.stderr)
        sys.exit(2)
    print(add(a, b))
    sys.exit(0)


if __name__ == "__main__":
    _cli()
