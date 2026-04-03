"""
Script to find the ASCII value of a character and vice versa.
Demonstrates the use of built-in functions ord() and chr().
"""

def get_ascii_value(char: str) -> int:
    """
    Returns the ASCII value of a single character using ord().
    """
    if len(char) != 1:
        raise ValueError("Input must be a single character.")
    return ord(char)

def get_char_from_ascii(ascii_val: int) -> str:
    """
    Returns the character for a given ASCII/Unicode value using chr().
    """
    if ascii_val < 0 or ascii_val > 1114111:
        raise ValueError("Invalid ASCII/Unicode value.")
    return chr(ascii_val)
