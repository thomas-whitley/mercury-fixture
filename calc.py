'''Simple calculator module.

Provides an `add` function that returns the sum of two integers and a command
line interface invoked via ``python -m calc add A B``.
'''

from __future__ import annotations

from typing import Any


def add(a: int, b: int) -> int:
    """Return the sum of two integers.

    The function is deliberately tiny so that it can be imported elsewhere
    without side‑effects.
    """
    return a + b


def _main() -> None:
    """Entry point for ``python -m calc``.

    Expected usage is ``python -m calc add A B`` where ``A`` and ``B`` are
    integer literals.  On success the sum is printed to *stdout* followed by a
    newline and the process exits with status ``0``.

    Any deviation – wrong sub‑command, wrong number of arguments, or non‑integer
    arguments – prints a helpful message to *stderr* and exits with status
    ``2``.
    """
    import sys

    args = sys.argv[1:]
    if len(args) != 3 or args[0] != "add":
        sys.stderr.write("Usage: python -m calc add A B\n")
        sys.exit(2)

    _, a_str, b_str = args
    try:
        a = int(a_str)
        b = int(b_str)
    except ValueError:
        sys.stderr.write("Both A and B must be integers.\n")
        sys.exit(2)

    result = add(a, b)
    # ``print`` adds a newline automatically.
    print(result)
    sys.exit(0)


if __name__ == "__main__":
    _main()
