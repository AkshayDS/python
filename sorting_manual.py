"""
Script to sort an array/list without using Python's built-in `sort()` or `sorted()` functions.
Demonstrates basic algorithms: Bubble Sort and Selection Sort.
"""

def bubble_sort(arr: list) -> list:
    """
    Sorts an array using the Bubble Sort algorithm.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    # Create a copy so we don't modify the original list in-place
    sorted_arr = arr.copy()
    
    for i in range(n):
        # Flag to optimize if already sorted
        swapped = False
        
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                # Swap elements
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
                
        # If no two elements were swapped by inner loop, then the array is sorted
        if not swapped:
            break
            
    return sorted_arr


def selection_sort(arr: list) -> list:
    """
    Sorts an array using the Selection Sort algorithm.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    sorted_arr = arr.copy()
    
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if sorted_arr[j] < sorted_arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element
        sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
        
    return sorted_arr


# --- Test Executions ---
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    
    print("--- Manual Array Sorting ---")
    print(f"Original Array: {test_array}\n")
    
    bubble_sorted = bubble_sort(test_array)
    print(f"Bubble Sort:    {bubble_sorted}")
    
    selection_sorted = selection_sort(test_array)
    print(f"Selection Sort: {selection_sorted}")
