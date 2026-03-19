"""
Script to check if a number is an Armstrong number.
An Armstrong number of n digits is an integer such that the sum of the nth powers of its digits is equal to the number itself.
Example: 153 = 1^3 + 5^3 + 3^3
"""

def is_armstrong_number(n: int) -> bool:
    """
    Checks if a number is an Armstrong number.
    """
    if n < 0:
        return False
        
    # Convert to string to find the number of digits (power)
    num_str = str(n)
    power = len(num_str)
    
    # Calculate sum of digits raised to the power
    total = sum(int(digit) ** power for digit in num_str)
    
    return total == n

def is_armstrong_number_math(n: int) -> bool:
    """
    Checks if a number is an Armstrong number using math operations.
    """
    if n < 0:
        return False
        
    original = n
    # Count digits
    count = 0
    temp = n
    while temp > 0:
        count += 1
        temp //= 10
        
    # Calculate sum
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit ** count
        temp //= 10
        
    return total == original
