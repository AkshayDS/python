"""
Script to check if two strings are anagrams of each other.
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
Example: "listen" and "silent"
"""
from collections import Counter

def is_anagram_sort(str1: str, str2: str) -> bool:
    """Checks for anagrams by sorting the cleaned strings. (O(n log n))"""
    clean_str1 = ''.join(char.lower() for char in str1 if char.isalnum())
    clean_str2 = ''.join(char.lower() for char in str2 if char.isalnum())
    
    return sorted(clean_str1) == sorted(clean_str2)

def is_anagram_counter(str1: str, str2: str) -> bool:
    """Checks for anagrams using Python's built-in Counter. (O(n))"""
    clean_str1 = ''.join(char.lower() for char in str1 if char.isalnum())
    clean_str2 = ''.join(char.lower() for char in str2 if char.isalnum())
    
    return Counter(clean_str1) == Counter(clean_str2)

# --- Test Executions ---
if __name__ == "__main__":
    test_cases = [
        ("listen", "silent"),
        ("rail safety", "fairy tales"),
        ("hello", "billion"),
        ("Dormitory", "Dirty room")
    ]
    
    print("--- Testing Anagrams (Python) ---")
    for s1, s2 in test_cases:
        sort_result = is_anagram_sort(s1, s2)
        counter_result = is_anagram_counter(s1, s2)
        
        print(f"\n'{s1}' & '{s2}':")
        print(f"  Sort Method:    {'✅ True' if sort_result else '❌ False'}")
        print(f"  Counter Method: {'✅ True' if counter_result else '❌ False'}")
