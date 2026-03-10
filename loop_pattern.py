"""
Script to demonstrate nested loops by printing a classic number triangle pattern.
Often used as a fundamental exercise in understanding loops.
"""

def print_number_triangle(rows: int) -> None:
    """
    Prints a right-angled triangle pattern of numbers using nested loops.
    Example for rows = 5:
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    """
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print() # Move to the next line after each row
