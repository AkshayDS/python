"""
Script to find the length of the longest substring without repeating characters.
Demonstrates the 'Sliding Window' technique using two pointers (left and right) 
and a Hash Set to track seen characters in O(n) optimal time.
"""

def length_of_longest_substring(s: str) -> int:
    """
    Finds the length of the longest continuous substring with no duplicate characters.
    """
    # Set to keep track of characters in our current window
    seen_chars = set()
    
    # Left pointer of our sliding window
    left = 0
    max_length = 0
    
    # Right pointer expands the window
    for right in range(len(s)):
        # If we see a duplicate character, we must shrink the window from the left
        # until the duplicate is removed from our current window set
        while s[right] in seen_chars:
            seen_chars.remove(s[left])
            left += 1
            
        # Add the new unique character to our window
        seen_chars.add(s[right])
        
        # Update our max length found so far
        # The size of our window is (right - left + 1)
        max_length = max(max_length, right - left + 1)
        
    return max_length
