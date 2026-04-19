"""
Script to count the occurrences of elements in a list.
Demonstrates iterative counting, frequency dictionaries, and built-in methods.
"""

def count_occurrences_manual(arr: list, target) -> int:
    """
    Counts the occurrences of a specific target manually by iterating over the list.
    """
    count = 0
    for item in arr:
        if item == target:
            count += 1
    return count

def count_occurrences_dict(arr: list) -> dict:
    """
    Counts the occurrences of all elements in the list using a frequency dictionary.
    Returns a dictionary where keys are elements and values are their frequencies.
    """
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    return freq

def count_occurrences_builtin(arr: list, target) -> int:
    """
    Counts occurrences of a specific target using the built-in list.count() method.
    """
    return arr.count(target)
