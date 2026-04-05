"""
Script to check if a number is a palindrome.
Demonstrates while loops and basic integer manipulation.
"""

def is_palindrome_number(n: int) -> bool:
    """
    Checks if a number is a palindrome by reversing the integer mathematically.
    """
    if n < 0:
        return False
        
    original = n
    reversed_num = 0
    
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
        
    return original == reversed_num

def is_palindrome_number_string(n: int) -> bool:
    """
    Checks if a number is a palindrome by converting it to a string.
    """
    if n < 0:
        return False
        
    str_n = str(n)
    return str_n == str_n[::-1]
