"""
Script to check if a number is a Strong Number.
A Strong Number is a number where the sum of the factorials of its digits 
is equal to the number itself. 
Example: 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145.
"""

def factorial(n: int) -> int:
    """Calculates the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_strong_number(n: int) -> bool:
    """Checks if the given number is a Strong Number."""
    if n == 0: # 0 is usually not considered a strong number as 0! = 1
        return False
    if n < 0:
        return False
        
    original_num = n
    sum_of_factorials = 0
    
    # Process each digit
    temp = n
    while temp > 0:
        digit = temp % 10
        sum_of_factorials += factorial(digit)
        temp //= 10
        
    return sum_of_factorials == original_num
