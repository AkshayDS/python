"""
Script to check if an array/list is sorted in ascending order.
Demonstrates array traversal, adjacent element comparison, and pythonic idioms.
"""

def is_sorted_iterative(arr: list) -> bool:
    """
    Checks if an array is sorted by manually comparing adjacent elements in a loop.
    """
    if not arr or len(arr) <= 1:
        return True
        
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
            
    return True

def is_sorted_pythonic(arr: list) -> bool:
    """
    Checks if an array is sorted using the all() function and generator expression.
    """
    if not arr or len(arr) <= 1:
        return True
        
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
