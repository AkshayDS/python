"""
Script to calculate the sum of natural numbers up to a given number n.
Demonstrates the use of a for loop and the mathematical formula.
Formula: n * (n + 1) / 2
"""

def sum_natural_numbers(n: int) -> int:
    """
    Calculates the sum of natural numbers up to n using a loop.
    """
    if n <= 0:
        return 0
        
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_natural_numbers_formula(n: int) -> int:
    """
    Calculates the sum of natural numbers up to n using the formula.
    """
    if n <= 0:
        return 0
    return n * (n + 1) // 2
