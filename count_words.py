"""
Script to count the number of words in a given string.
Demonstrates the use of `.split()`.
"""

def count_words(s: str) -> int:
    """
    Counts words in a string by splitting by whitespace.
    """
    if not s.strip():
        return 0
    return len(s.split())

def count_words_manual(s: str) -> int:
    """
    Counts words manually by iterating through characters.
    """
    count = 0
    in_word = False
    
    for char in s:
        if char.isspace():
            in_word = False
        elif not in_word:
            count += 1
            in_word = True
            
    return count
