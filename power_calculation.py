"""
Script to calculate the power of a number (x^n) without using ** or pow().
Demonstrates loops and recursion.
"""

def power_loop(base: int, exp: int) -> int:
    """
    Calculates base^exp using a loop.
    """
    result = 1
    for _ in range(abs(exp)):
        result *= base
    if exp < 0:
        return 1 / result
    return result

def power_recursive(base: int, exp: int) -> int:
    """
    Calculates base^exp using recursion.
    """
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power_recursive(base, -exp)
    return base * power_recursive(base, exp - 1)
