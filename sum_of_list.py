"""
Script to calculate the sum of elements in a list.
Demonstrates the use of a simple for loop to aggregate values.
"""

def sum_list(arr: list) -> int:
    """
    Calculates the sum of all elements in a given list.
    """
    total = 0
    for num in arr:
        total += num
    return total

def sum_list_built_in(arr: list) -> int:
    """
    Calculates the sum of all elements using Python's built-in `sum()` function.
    """
    return sum(arr)
