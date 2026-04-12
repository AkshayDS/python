"""
Script to find the first non-repeating character in a string.
Demonstrates the use of frequency dictionaries and two-pass string iteration.
"""

def first_non_repeating_char(text: str) -> str:
    """
    Returns the first non-repeating character in a string.
    Returns None if all characters repeat or the string is empty.
    """
    char_counts = {}
    
    # First pass: count frequencies of each character
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
        
    # Second pass: find the first character with a frequency of exactly 1
    for char in text:
        if char_counts[char] == 1:
            return char
            
    return None
