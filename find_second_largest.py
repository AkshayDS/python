"""
Script to find the second largest number in an array without using sorting 
or built-in functions like max().
Implemented in the simplest and most efficient way (O(n) time complexity).
"""

def find_second_largest(arr: list) -> int:
    """
    Finds the second largest unique number in an array.
    Returns None if the array has less than 2 unique elements.
    """
    if len(arr) < 2:
        return None
        
    largest = arr[0]
    second_largest = None
    
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        num = arr[i]
        
        # If we find a new largest number, the old largest becomes second largest
        if num > largest:
            second_largest = largest
            largest = num
            
        # If it's not larger than the largest, but larger than the current second largest
        # and it's not equal to the largest itself (to handle duplicates)
        elif num != largest:
            if second_largest is None or num > second_largest:
                second_largest = num
                
    return second_largest


# --- Test Executions ---
if __name__ == "__main__":
    test_cases = [
        [10, 5, 20, 8, 12],          # Basic case
        [10, 10, 10],                # All duplicates
        [50, 40, 50, 30],            # Duplicates of the largest
        [1, 2],                      # Smallest valid array
        [5]                          # Invalid array
    ]
    
    print("--- Find Second Largest Number ---")
    
    for case in test_cases:
        result = find_second_largest(case)
        print(f"Array: {case}")
        print(f" -> Second Largest: {result}\n")
