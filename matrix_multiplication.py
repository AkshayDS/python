"""
Script to perform matrix multiplication.
Demonstrates constraints checking and multi-level nested loops.
"""

def multiply_matrices(mat1: list, mat2: list) -> list:
    """
    Multiplies two compatible matrices using nested loops.
    Returns a new matrix containing the product.
    The number of columns in the first matrix must equal the number of rows in the second.
    """
    # Check for empty matrices or incompatible dimensions
    if not mat1 or not mat2 or not mat1[0] or len(mat1[0]) != len(mat2):
        return []
        
    rows1 = len(mat1)
    cols1 = len(mat1[0])
    cols2 = len(mat2[0])
    
    # Initialize the result matrix with zeros (dimensions: rows1 x cols2)
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    # Iterate through rows of mat1
    for i in range(rows1):
        # Iterate through columns of mat2
        for j in range(cols2):
            # Iterate through rows of mat2 (or columns of mat1)
            for k in range(cols1):
                result[i][j] += mat1[i][k] * mat2[k][j]
                
    return result
