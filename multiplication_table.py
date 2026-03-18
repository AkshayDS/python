"""
Script to print the multiplication table of a given number.
Demonstrates the use of a simple for loop.
"""

def print_multiplication_table(n: int, up_to: int = 10):
    """
    Prints the multiplication table of n up to the specified limit.
    """
    for i in range(1, up_to + 1):
        print(f"{n} x {i} = {n * i}")

def get_multiplication_table_list(n: int, up_to: int = 10) -> list:
    """
    Returns the multiplication table values as a list.
    """
    return [n * i for i in range(1, up_to + 1)]
