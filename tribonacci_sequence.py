"""
Script to generate the Tribonacci sequence.
The Tribonacci sequence is a series of numbers where each term is the sum 
of the preceding three terms.
The sequence typically starts with 0, 0, 1.

Example: 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, ...
"""

def generate_tribonacci(n: int) -> list:
    """
    Generates the first n terms of the Tribonacci sequence.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 0]
    elif n == 3:
        return [0, 0, 1]
        
    sequence = [0, 0, 1]
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2] + sequence[-3]
        sequence.append(next_term)
        
    return sequence

if __name__ == "__main__":
    n_terms = 10
    print(f"First {n_terms} terms of Tribonacci sequence:")
    print(generate_tribonacci(n_terms))
