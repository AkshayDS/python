"""
Script to demonstrate the classic Binary Search algorithm.
This algorithm efficiently finds the position of a target value within a *sorted* array.
It works by repeatedly dividing the search interval in half, achieving an O(log n) time complexity.
"""

def binary_search(arr: list, target: int) -> int:
    """
    Searches for a target value in a sorted array.
    Returns the index of the target if found, otherwise returns -1.
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        # Find the middle element of the current search interval
        mid = (left + right) // 2
        
        # Check if the target is found at the mid index
        if arr[mid] == target:
            return mid
            
        # If the target is greater than the mid element, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
            
        # If the target is smaller than the mid element, ignore the right half
        else:
            right = mid - 1
            
    # Target was not found in the array
    return -1
