'''A deliberately small module for Mercury's repo chore integration test to edit.'''


def add(a: int, b: int) -> int:
    return a + b


def clamp(value, low, high):
    if low > high:
        raise ValueError
    return max(low, min(high, value))
