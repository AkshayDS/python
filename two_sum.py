"""
Script to find two numbers in an array that add up to a specific target sum.
Demonstrates the use of a Hash Map (Python dictionary) for O(n) time complexity lookups.
"""

def two_sum(arr: list, target: int) -> list:
    """
    Finds the indices of two numbers that add up to the target sum.
    Uses a dictionary to store the numbers seen so far and their indices.
    """
    seen_numbers = {}  # Map to store {number: index}
    
    for current_index, current_number in enumerate(arr):
        # Calculate the number needed to reach the target sum
        complement = target - current_number
        
        # Check if we have already seen the complement
        if complement in seen_numbers:
            # If so, return the indices of both numbers
            return [seen_numbers[complement], current_index]
            
        # If not, store the current number and its index for future lookups
        seen_numbers[current_number] = current_index
        
    # Return empty list if no two numbers sum up to the target
    return []
