"""
Script to count the number of vowels in a given string.
Demonstrates string iteration, case-insensitivity handling, and checking against a set for O(1) lookups.
"""

def count_vowels(text: str) -> int:
    """
    Counts the number of vowels (a, e, i, o, u) in a string.
    """
    vowels = set("aeiouAEIOU")
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
            
    return count
