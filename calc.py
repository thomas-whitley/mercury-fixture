"""A deliberately small module for Mercury's repo chore integration test to edit."""

import sys


def add(a: int, b: int) -> int:
    return a + b


def main():
    if len(sys.argv) != 4 or sys.argv[1] != "add":
        sys.stderr.write("Usage: python -m calc add A B\n")
        sys.exit(2)
    try:
        a = int(sys.argv[2])
        b = int(sys.argv[3])
    except ValueError:
        sys.stderr.write("Error: arguments must be integers\n")
        sys.exit(2)
    
    result = add(a, b)
    sys.stdout.write(f"{result}\n")
    sys.exit(0)


if __name__ == "__main__":
    main()
