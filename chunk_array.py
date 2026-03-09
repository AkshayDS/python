"""
Script to divide an array into smaller chunks of a specified size.
Implemented in the simplest way using Python's list comprehension.
"""

def chunk_array(arr: list, chunk_size: int) -> list:
    """
    Subdivides a list into multiple sub-lists of a specified maximum size.
    """
    if chunk_size <= 0:
        return []
        
    return [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]
