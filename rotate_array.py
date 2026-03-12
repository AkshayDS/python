"""
Script to rotate an array to the right by k steps.
Demonstrates three approaches:
1. Using slicing (Pythonic)
2. Using an auxiliary array
3. In-place using reversal (O(1) space)
"""

def rotate_array_slicing(nums: list, k: int) -> None:
    """
    Rotates the array in-place using slicing.
    """
    n = len(nums)
    if n == 0: return
    k = k % n
    nums[:] = nums[n-k:] + nums[:n-k]

def rotate_array_inplace(nums: list, k: int) -> None:
    """
    Rotates the array in-place with O(1) extra space using the reversal method.
    """
    n = len(nums)
    if n == 0: return
    k = k % n
    
    def reverse(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            
    # Reverse the entire array
    reverse(0, n - 1)
    # Reverse the first k elements
    reverse(0, k - 1)
    # Reverse the remaining n-k elements
    reverse(k, n - 1)
