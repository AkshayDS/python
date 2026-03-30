"""
Script to find the GCD (Greatest Common Divisor) and LCM (Least Common Multiple) of two numbers.
Demonstrates Euclidean algorithm.
"""

def gcd(a: int, b: int) -> int:
    """
    Finds GCD using the Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """
    Finds LCM using the relation: LCM(a, b) = (a * b) / GCD(a, b).
    """
    return abs(a * b) // gcd(a, b)
