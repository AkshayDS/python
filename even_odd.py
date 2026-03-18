"""
Script to check if a number is even or odd.
Demonstrates the use of the modulo `%` operator.
"""

def is_even(n: int) -> bool:
    """
    Returns True if n is even, False otherwise.
    """
    return n % 2 == 0

def check_even_odd(n: int) -> str:
    """
    Returns 'Even' or 'Odd' string for given number.
    """
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
