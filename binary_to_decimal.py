"""
Script to convert a binary string to a decimal integer.
Demonstrates manual base conversion and built-in function usage.
"""

def binary_to_decimal_manual(binary_str: str) -> int:
    """
    Converts binary to decimal using manual positional values.
    """
    if not binary_str:
        return 0
        
    decimal = 0
    # Reverse string to easily iterate from 0 to n powers
    for i, digit in enumerate(binary_str[::-1]):
        if digit == '1':
            decimal += 2 ** i
        elif digit != '0':
            raise ValueError(f"Invalid binary string: contains character '{digit}'")
            
    return decimal

def binary_to_decimal_builtin(binary_str: str) -> int:
    """
    Converts binary to decimal using the built-in int() function with base 2.
    """
    return int(binary_str, 2)
