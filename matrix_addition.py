"""
Script to perform addition of two matrices.
Demonstrates the use of nested loops and nested list comprehensions.
"""

def add_matrices_loops(mat1: list, mat2: list) -> list:
    """
    Adds two equally sized matrices using nested for loops.
    Returns a new matrix containing the sums.
    """
    if not mat1 or not mat2 or len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return []
        
    result = []
    # Iterate through rows
    for i in range(len(mat1)):
        row_sum = []
        # Iterate through columns
        for j in range(len(mat1[0])):
            row_sum.append(mat1[i][j] + mat2[i][j])
        result.append(row_sum)
        
    return result

def add_matrices_comprehensions(mat1: list, mat2: list) -> list:
    """
    Adds two matrices using nested list comprehensions.
    This is generally more pythonic and concise.
    """
    if not mat1 or not mat2 or len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return []
        
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
