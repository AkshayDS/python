"""
Script to find common elements between two lists.
Demonstrates set intersection and manual iteration.
"""

def common_elements_set(lst1: list, lst2: list) -> list:
    """
    Finds common elements using set intersection.
    """
    return list(set(lst1) & set(lst2))

def common_elements_loop(lst1: list, lst2: list) -> list:
    """
    Finds common elements using a loop (preserves order).
    """
    result = []
    for item in lst1:
        if item in lst2 and item not in result:
            result.append(item)
    return result
