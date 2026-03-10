"""
Script to generate the Fibonacci sequence up to a specified number of terms.
Implemented using an iterative approach for O(n) time complexity and O(n) space complexity.
"""

def generate_fibonacci(n: int) -> list:
    """
    Generates a list containing the first 'n' numbers of the Fibonacci sequence.
    The sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
        
    # Initialize the sequence with the first two numbers
    sequence = [0, 1]
    
    # Iteratively calculate the next numbers in the sequence
    for _ in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
        
    return sequence
