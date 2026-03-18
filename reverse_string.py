"""
Script to reverse a string.
Demonstrates the use of slicing and a loop approach.
"""

def reverse_string_slicing(s: str) -> str:
    """
    Reverses a string using Python's slicing technique `[::-1]`.
    """
    return s[::-1]

def reverse_string_loop(s: str) -> str:
    """
    Reverses a string using a simple loop.
    """
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
