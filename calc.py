def clamp(value, low, high):
    if low > high:
        raise ValueError('low cannot be greater than high')
    return max(min(value, high), low)

from typing import *


def add(a: int, b: int) -> int:
    return a + b