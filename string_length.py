"""
Script to find the length of a string without using the built-in len() function.
Demonstrates iteration over a string.
"""

def get_string_length(s: str) -> int:
    """
    Calculates the length of a string without len().
    """
    count = 0
    for _ in s:
        count += 1
    return count

def get_string_length_while(s: str) -> int:
    """
    Calculates the length of a string using a while loop (less common in Python).
    """
    count = 0
    while True:
        try:
            _ = s[count]
            count += 1
        except IndexError:
            break
    return count
