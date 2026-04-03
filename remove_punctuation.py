"""
Script to remove punctuation from a given string.
Demonstrates the use of string methods and list comprehensions.
"""
import string

def remove_punctuation(text: str) -> str:
    """
    Removes punctuation using string.punctuation and list comprehension.
    """
    return "".join(char for char in text if char not in string.punctuation)

def remove_punctuation_translate(text: str) -> str:
    """
    Removes punctuation using the str.translate method.
    """
    return text.translate(str.maketrans('', '', string.punctuation))
