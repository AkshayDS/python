"""
Script to reverse an array in-place without using Python's built-in `.reverse()` 
or list slicing like `[::-1]`.
Implemented using the optimal O(n) two-pointer approach with O(1) space complexity.
"""

def reverse_array(arr: list) -> list:
    """
    Reverses the elements of an array in-place.
    Returns the modified array.
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # Swap the elements at the left and right pointers
        arr[left], arr[right] = arr[right], arr[left]
        
        # Move pointers towards the middle
        left += 1
        right -= 1
        
    return arr
