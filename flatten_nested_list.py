"""
Script to flatten a nested list into a single list.
Demonstrates recursion and list comprehension.
"""

def flatten_list(lst: list) -> list:
    """
    Flattens a nested list using recursion.
    """
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def flatten_list_iterative(lst: list) -> list:
    """
    Flattens a nested list using a stack (iterative).
    """
    stack = list(lst)
    result = []
    while stack:
        item = stack.pop(0)
        if isinstance(item, list):
            stack = item + stack
        else:
            result.append(item)
    return result
