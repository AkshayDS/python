"""
Script to swap two variables.
Demonstrates the use of a temporary variable and Python's tuple unpacking.
"""

def swap_with_temp(a, b) -> tuple:
    """
    Swaps two variables using a temporary variable.
    """
    temp = a
    a = b
    b = temp
    return a, b

def swap_without_temp(a, b) -> tuple:
    """
    Swaps two variables without a temporary variable (Python trick).
    """
    a, b = b, a
    return a, b
