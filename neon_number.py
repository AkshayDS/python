"""
Script to check if a number is a Neon Number.
A neon number is a number where the sum of digits of the square of the number 
is equal to the number itself.

Example: 9 is a neon number.
9^2 = 81
8 + 1 = 9
"""

def is_neon_number(n: int) -> bool:
    """
    Returns True if n is a neon number, otherwise False.
    """
    if n < 0:
        return False
        
    sq_n = n * n
    digit_sum = 0
    
    # Calculate sum of digits of the square
    while sq_n > 0:
        digit_sum += sq_n % 10
        sq_n //= 10
        
    return digit_sum == n

if __name__ == "__main__":
    test_numbers = [9, 1, 0, 12, 10]
    for num in test_numbers:
        print(f"Is {num} a Neon Number? {is_neon_number(num)}")
