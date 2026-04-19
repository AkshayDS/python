"""
Script to find the longest word in a string or sentence.
Demonstrates string manipulation, splitting, iteration, and using built-in functions.
"""

def find_longest_word(text: str) -> str:
    """
    Finds the longest word iteratively by checking each word's length.
    """
    if not text:
        return ""
        
    # Split the string into a list of words (default separator is whitespace)
    words = text.split()
    longest = ""
    
    for word in words:
        if len(word) > len(longest):
            longest = word
            
    return longest

def find_longest_word_pythonic(text: str) -> str:
    """
    Finds the longest word using Python's built-in max() function
    by providing 'len' as the sorting key.
    """
    if not text:
        return ""
        
    words = text.split()
    # The key parameter tells max() to evaluate each item using the len() function
    return max(words, key=len)
