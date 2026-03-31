"""
Script to sort a list without using the built-in sort() function.
Demonstrates Bubble Sort algorithm.
"""

def bubble_sort(lst: list) -> list:
    """
    Sorts a list using Bubble Sort.
    """
    arr = lst.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(lst: list) -> list:
    """
    Sorts a list using Selection Sort.
    """
    arr = lst.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
