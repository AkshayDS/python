"""
Script to calculate the mean (average) of a list of numbers.
Demonstrates manual iterative summation alongside native built-in function approaches.
"""

def get_mean_iterative(arr: list) -> float:
    """
    Calculates the mean by manually iterating over the list and summing elements.
    Returns 0.0 if the array is empty.
    """
    if not arr:
        return 0.0
        
    total = 0
    count = 0
    for num in arr:
        total += num
        count += 1
        
    return total / count

def get_mean_builtin(arr: list) -> float:
    """
    Calculates the mean using Python's built-in sum() and len() computations.
    """
    if not arr:
        return 0.0
        
    return sum(arr) / len(arr)
