"""
Script to check if a given integer is a power of two.
Demonstrates:
1. Iterative approach (successive division by 2)
2. Bitwise approach (highly efficient O(1) time)
"""

def is_power_of_two_iterative(n: int) -> bool:
    """
    Checks if n is a power of two using iteration.
    """
    if n <= 0:
        return False
    while n % 2 == 0:
        n //= 2
    return n == 1

def is_power_of_two_bitwise(n: int) -> bool:
    """
    Checks if n is a power of two using a bitwise trick.
    A power of two in binary has exactly one bit set (e.g., 8 is 1000).
    n & (n - 1) will be 0 if n is a power of two.
    """
    return n > 0 and (n & (n - 1)) == 0
