"""
Script to find the intersection of two arrays (common elements) without using built-in set operations.
Implemented in a straightforward way to maintain order and handle potential duplicates based on requirements.
"""

def array_intersection(arr1: list, arr2: list) -> list:
    """
    Finds common elements between two arrays without using Python's built-in `set()`.
    Returns a list of unique common elements.
    """
    intersection = []
    
    for item in arr1:
        # Check if the item is in the second array and not already in our result
        if item in arr2 and item not in intersection:
            intersection.append(item)
            
    return intersection
