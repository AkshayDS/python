"""
Script to find the Greatest Common Divisor (GCD) of two numbers.
Demonstrates the Euclidean Algorithm, which is an efficient method 
operating in O(log(min(a, b))) time complexity.
"""

def find_gcd(a: int, b: int) -> int:
    """
    Calculates the Greatest Common Divisor of two integers using iteration.
    Based on the property: gcd(a, b) = gcd(b, a % b).
    """
    while b:
        a, b = b, a % b
    return abs(a)

def find_gcd_recursive(a: int, b: int) -> int:
    """
    Calculates the GCD using a recursive implementation of the Euclidean Algorithm.
    """
    if b == 0:
        return abs(a)
    return find_gcd_recursive(b, a % b)
