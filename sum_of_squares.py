"""
Script to calculate the sum of squares of the first n natural numbers.
Demonstrates iterative approach and a direct mathematical formula.
"""

def sum_of_squares_iterative(n: int) -> int:
    """
    Calculates the sum of squares using a loop.
    For example: if n = 3, calculates 1^2 + 2^2 + 3^2 = 14
    """
    if n <= 0:
        return 0
        
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

def sum_of_squares_formula(n: int) -> int:
    """
    Calculates the sum of squares using the mathematical formula:
    [n * (n + 1) * (2n + 1)] / 6
    """
    if n <= 0:
        return 0
        
    return (n * (n + 1) * (2 * n + 1)) // 6
