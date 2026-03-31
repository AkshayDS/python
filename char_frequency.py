"""
Script to count the frequency of each character in a string.
Demonstrates the use of dictionaries.
"""

def char_frequency(s: str) -> dict:
    """
    Counts the frequency of each character using a dictionary.
    """
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

def char_frequency_get(s: str) -> dict:
    """
    Counts frequency using dict.get() method.
    """
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq
