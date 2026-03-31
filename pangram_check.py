"""
Script to check if a string is a pangram.
A pangram is a sentence that contains every letter of the alphabet at least once.
Example: "The quick brown fox jumps over the lazy dog"
"""

def is_pangram(s: str) -> bool:
    """
    Checks if a string is a pangram using a set.
    """
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet.issubset(set(s.lower()))

def is_pangram_loop(s: str) -> bool:
    """
    Checks if a string is a pangram using a loop.
    """
    s = s.lower()
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        if ch not in s:
            return False
    return True
