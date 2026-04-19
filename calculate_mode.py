"""
Script to calculate the mode (most frequent element) of a list of numbers.
Demonstrates frequency counting via dictionaries and filtering via list comprehensions.
"""

def get_modes(arr: list) -> list:
    """
    Calculates the mode(s) of an array/list.
    Because a dataset can be multi-modal, this returns a list of all elements
    sharing the highest frequency. returns an empty list if given array is empty.
    """
    if not arr:
        return []
        
    # Count frequencies of each number
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        
    # Find the maximum frequency count that any number achieved
    max_count = max(freq.values())
    
    # Extract all numbers that have this maximum frequency count
    modes = [num for num, count in freq.items() if count == max_count]
    
    return modes
