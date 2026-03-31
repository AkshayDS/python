"""
Script to find the second largest number in a list.
Demonstrates iteration and comparison logic.
"""

def second_largest(lst: list) -> int:
    """
    Finds the second largest number using sorting.
    """
    if len(lst) < 2:
        return None
    unique = list(set(lst))
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[-2]

def second_largest_loop(lst: list) -> int:
    """
    Finds the second largest number using a single pass.
    """
    if len(lst) < 2:
        return None
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None
