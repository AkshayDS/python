"""
Script to perform a linear search on a list.
Demonstrates basic array traversal to find a target element.
"""

def linear_search_index(arr: list, target) -> int:
    """
    Searches for a target element in a list sequentially using index reference.
    Returns the index of the element if found, or -1 if not found.
    """
    if not arr:
        return -1
        
    for i in range(len(arr)):
        if arr[i] == target:
            return i
            
    return -1

def linear_search_enumerate(arr: list, target) -> int:
    """
    Searches for a target element using the pythonic enumerate() function.
    Returns the index of the element if found, or -1 if not found.
    """
    if not arr:
        return -1
        
    for index, value in enumerate(arr):
        if value == target:
            return index
            
    return -1
