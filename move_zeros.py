"""
Script to move all zeros in an array to the end while maintaining the relative order of the non-zero elements.
Implemented in the simplest way using the two-pointer approach for O(n) time and O(1) space complexity.
"""

def move_zeros(arr: list) -> list:
    """
    Moves all zeros to the end of the array in-place.
    """
    non_zero_index = 0
    
    # Move all non-zero elements to the front
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1
            
    # Fill the remaining array with zeros
    for i in range(non_zero_index, len(arr)):
        arr[i] = 0
        
    return arr
