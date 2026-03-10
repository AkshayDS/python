"""
Script to find the majority element in an array (the element that appears more than n/2 times).
Implemented using the Boyer-Moore Voting Algorithm for O(n) time and O(1) space complexity.
"""

def find_majority_element(arr: list) -> int:
    """
    Finds and returns the majority element in an array.
    Assumes that a majority element always exists in the input array.
    """
    candidate = None
    count = 0
    
    # Phase 1: Find a candidate for the majority element
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
            
    # Phase 2: The candidate is guaranteed to be the majority element
    # based on the assumption that one always exists
    return candidate
