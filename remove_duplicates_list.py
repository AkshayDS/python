"""
Script to remove duplicate elements from a list.
Demonstrates the use of sets and manual iteration.
"""

def remove_duplicates_set(lst: list) -> list:
    """
    Removes duplicates using a set (order not preserved).
    """
    return list(set(lst))

def remove_duplicates_ordered(lst: list) -> list:
    """
    Removes duplicates while preserving the original order.
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
