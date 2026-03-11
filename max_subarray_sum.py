"""
Script to find the maximum sum of any contiguous subarray of size 'k'.
Demonstrates the classic 'Sliding Window' algorithmic technique.
Instead of recalculating the sum of every subarray from scratch (which is O(n*k)),
it slides a window across the array, adding the new element and removing the old one in O(n) time.
"""

def max_subarray_sum(arr: list, k: int) -> int:
    """
    Finds the maximum sum of a contiguous subarray of size k.
    """
    n = len(arr)
    
    # Return 0 if the array is empty or if k is invalid
    if n == 0 or k <= 0 or k > n:
        return 0
        
    # Calculate the sum of the first 'window' of size k
    current_window_sum = sum(arr[:k])
    max_sum = current_window_sum
    
    # Slide the window across the rest of the array
    for i in range(n - k):
        # Subtract the element that is falling out of the window 
        # and add the new element coming into the window
        current_window_sum = current_window_sum - arr[i] + arr[i + k]
        
        # Update max_sum if the current window's sum is larger
        if current_window_sum > max_sum:
            max_sum = current_window_sum
            
    return max_sum
