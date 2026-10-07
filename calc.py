def clamp(value, low, high):
    if low > high:
        raise ValueError('low cannot be greater than high')
    return max(min(value, high), low)

def add(a, b):
    return a + b