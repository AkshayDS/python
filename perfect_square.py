"""
Script to check if a number is a Perfect Square.
A Perfect Square is an integer that is the square of an integer.
Example: 16 (4*4), 25 (5*5), 0 (0*0), 1 (1*1).
"""
import math

def is_perfect_square(n: int) -> bool:
    """
    Checks if a given number is a perfect square.
    """
    if n < 0:
        return False
    
    # Using math.isqrt for integer square root in Python 3.8+
    sqrt_n = math.isqrt(n)
    return sqrt_n * sqrt_n == n

def is_perfect_square_alternative(n: int) -> bool:
    """
    Alternative method using math.sqrt and floor comparison.
    """
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    
    sqrt_n = math.sqrt(n)
    return sqrt_n == int(sqrt_n)

if __name__ == "__main__":
    test_cases = [16, 25, 14, 10, 0, 1, 99, 100]
    for num in test_cases:
        print(f"Is {num} a perfect square? {is_perfect_square(num)}")
