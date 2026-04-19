"""
Script to calculate the median value of a list of numbers.
Demonstrates list sorting, mathematical array properties, and conditional logic.
"""

def get_median(arr: list) -> float:
    """
    Calculates the median of an array/list.
    Returns 0.0 if the array is empty.
    """
    if not arr:
        return 0.0
        
    # Sort the array so that we can find the exact middle relative to the set's magnitude
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    mid = n // 2
    
    if n % 2 == 0:
        # If the list length is even, the median is the average of the two middle elements.
        return (sorted_arr[mid - 1] + sorted_arr[mid]) / 2.0
    else:
        # If the list length is odd, the median is exactly the center element.
        return float(sorted_arr[mid])
