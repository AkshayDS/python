"""
Script to find all factors of a given number.
Demonstrates the use of loops and an optimized algorithmic approach.
"""

def get_factors(n: int) -> list:
    """
    Returns a list containing all the factors of a number.
    Uses a standard iterative approach.
    """
    factors = []
    if n <= 0:
        return factors
        
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
            
    return factors

def get_factors_optimized(n: int) -> list:
    """
    Returns a list of factors of a number using an optimized loop.
    Iterates only up to the square root of n.
    """
    factors = set()
    if n <= 0:
        return list(factors)
        
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
            
    return sorted(list(factors))
