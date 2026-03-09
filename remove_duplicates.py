"""
Script to remove duplicates from an array while maintaining the original order.
Implemented in the simplest O(n) way using a set to track seen elements.
"""

def remove_duplicates(arr: list) -> list:
    """
    Removes duplicate elements from a list while preserving the order of first occurrences.
    """
    seen = set()
    result = []
    
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
            
    return result
