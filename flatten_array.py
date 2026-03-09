"""
Script to flatten a nested array (list of lists) into a single continuous list.
Implemented in the simplest way using recursion.
"""

def flatten_array(nested_list: list) -> list:
    """
    Takes a list that might contain other lists and flattens it completely.
    """
    flat_list = []
    
    for item in nested_list:
        if type(item) is list:
            # If the item is a list, recursively flatten it and extend the main list
            flat_list.extend(flatten_array(item))
        else:
            # If it's a normal element, just append it
            flat_list.append(item)
            
    return flat_list
