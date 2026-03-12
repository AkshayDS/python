"""
Script to merge two sorted arrays into a single sorted array.
Demonstrates the two-pointer technique for O(n+m) time complexity.
"""

def merge_sorted_arrays(arr1: list, arr2: list) -> list:
    """
    Merges two sorted lists into a new sorted list.
    """
    merged = []
    i = 0  # Pointer for arr1
    j = 0  # Pointer for arr2
    
    # Traverse both arrays and pick the smaller element to add to merged
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
            
    # Append remaining elements from arr1 if any
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
        
    # Append remaining elements from arr2 if any
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
        
    return merged
