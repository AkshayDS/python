"""
Script to reverse the order of words in a given string.
Demonstrates the use of string split() and join() methods.
"""

def reverse_words_builtin(text: str) -> str:
    """
    Reverses words using python's built-in string methods and slicing.
    """
    # split() without arguments splits by whitespace and handles multiple spaces
    return " ".join(text.split()[::-1])

def reverse_words_manual(text: str) -> str:
    """
    Reverses words manually using a loop.
    """
    words = text.split()
    reversed_words = []
    for i in range(len(words) - 1, -1, -1):
        reversed_words.append(words[i])
    
    return " ".join(reversed_words)
