"""
Script to calculate the sum of digits of a given number.
Demonstrates the use of modulo `%` and floor division `//`.
"""

def sum_of_digits(n: int) -> int:
    """
    Calculates the sum of digits of an integer.
    """
    total = 0
    # Handle negative numbers
    n = abs(n)
    
    while n > 0:
        total += n % 10
        n //= 10
        
    return total

def sum_of_digits_str(n: int) -> int:
    """
    Calculates the sum of digits using string conversion.
    """
    total = 0
    for digit in str(abs(n)):
        total += int(digit)
    return total
