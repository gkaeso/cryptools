def gcd(a: int, b: int) -> int:
    """This function returns the greatest common divisor between two given integers."""
    if a < 1 or b < 1:
        raise ValueError(f'Input arguments (a={a}, b={b}) must be positive integers')
    while a != 0:
        a, b = b % a, a
    return b
