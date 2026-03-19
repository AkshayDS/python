"""
Script to check if a character is a vowel or a consonant.
Demonstrates the use of membership operators ('in') and string methods.
"""

def check_vowel_consonant(ch: str) -> str:
    """
    Checks if a character is a vowel, consonant, or not an alphabet.
    """
    if not ch.isalpha():
        return "Not an alphabet"
        
    lower_ch = ch.lower()
    vowels = 'aeiou'
    
    if lower_ch in vowels:
        return "Vowel"
    else:
        return "Consonant"

def check_vowel_consonant_set(ch: str) -> str:
    """
    Checks if a character is a vowel or consonant using a set.
    """
    if not ch.isalpha():
        return "Not an alphabet"
        
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    
    if ch in vowels:
        return "Vowel"
    else:
        return "Consonant"
