"""
Script to find the minimum and maximum elements in a list.
Demonstrates the use of a for loop and conditional statement.
"""

def find_min_max(arr: list) -> tuple:
    """
    Finds and returns the (min, max) elements of a list.
    """
    if not arr:
        return None, None
        
    min_val = arr[0]
    max_val = arr[0]
    
    for num in arr[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
            
    return min_val, max_val

def find_min_max_built_in(arr: list) -> tuple:
    """
    Finds minimum and maximum using Python's built-in `min()` and `max()`.
    """
    if not arr:
        return None, None
    return min(arr), max(arr)
