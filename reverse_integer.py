"""
Script to reverse the digits of an integer.
Implemented using mathematical operations (modulo and floor division) 
rather than converting the integer to a string.
"""

def reverse_integer(n: int) -> int:
    """
    Reverses an integer mathematically.
    Handles negative numbers and preserves the sign.
    """
    is_negative = n < 0
    
    # Work with the absolute value to make the math easier
    n = abs(n)
    reversed_num = 0
    
    while n > 0:
        # Get the last digit of the current number
        digit = n % 10
        # Add the digit to the reversed number (shifting existing digits left)
        reversed_num = (reversed_num * 10) + digit
        # Remove the last digit from the original number
        n = n // 10
        
    return -reversed_num if is_negative else reversed_num
