"""
Script to determine if a given number is a prime number.
Implemented using the optimal O(sqrt(n)) time complexity approach.
"""

import math

def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.
    A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.
    """
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
        
    # 2 and 3 are prime numbers
    if n <= 3:
        return True
        
    # Eliminate numbers divisible by 2 or 3 to save loop iterations
    if n % 2 == 0 or n % 3 == 0:
        return False
        
    # Check for factors from 5 up to the square root of n
    # We step by 6 because all primes greater than 3 can be written as 6k +/- 1
    limit = int(math.sqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
            
    return True
