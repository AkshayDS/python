"""
Script to find the union of two lists.
The union contains all unique elements that are present in at least one of the lists.
"""

def union_of_lists_set(lst1: list, lst2: list) -> list:
    """
    Returns the union of two lists using the set union operator.
    Does not preserve order.
    """
    return list(set(lst1) | set(lst2))

def union_of_lists_manual(lst1: list, lst2: list) -> list:
    """
    Returns the union of two lists manually while preserving original order.
    Iterates through both lists and adds elements if they aren't already present.
    """
    union = []
    # Add elements from the first list
    for item in lst1:
        if item not in union:
            union.append(item)
            
    # Add elements from the second list
    for item in lst2:
        if item not in union:
            union.append(item)
            
    return union
