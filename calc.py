"""A deliberately small module for Mercury's repo chore integration test to edit."""


def add(a: int, b: int) -> int:
    return a + b


def divide(a, b) -> float:
    if b == 0:
        raise ValueError("cannot divide by zero")
    return float(a / b)
