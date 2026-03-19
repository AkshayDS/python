"""
Script to check if a number is a Perfect Number.
A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).
Example: 6 = 1 + 2 + 3
"""

def is_perfect_number(n: int) -> bool:
    """
    Checks if a number is a perfect number.
    """
    if n <= 0:
        return False
        
    total = 0
    # Find divisors from 1 to n/2
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total += i
            
    return total == n

def get_perfect_numbers_in_range(start: int, end: int) -> list:
    """
    Returns a list of perfect numbers in the given range.
    """
    return [num for num in range(start, end + 1) if is_perfect_number(num)]
