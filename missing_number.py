"""
Script to find the missing number in an array containing distinct numbers from 1 to N.
Using the simplest mathematical formula: Sum of first N natural numbers = n * (n + 1) / 2
"""

def find_missing_number(arr: list) -> int:
    """
    Finds the missing number in an array of integers sequence from 1 to N.
    """
    if not arr:
        return 1
        
    n = len(arr) + 1  # Missing one element, so total elements should be length + 1
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(arr)
    
    return expected_sum - actual_sum
