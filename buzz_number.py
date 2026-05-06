"""
Script to check if a number is a Buzz Number.
A Buzz number is a number that ends with 7 or is divisible by 7.

Example: 7, 14, 17, 27, 28 are Buzz numbers.
"""

def is_buzz_number(n: int) -> bool:
    """
    Returns True if n is a buzz number, otherwise False.
    """
    if n < 0:
        return False
        
    # Check if divisible by 7 or ends with 7
    return n % 7 == 0 or n % 10 == 7

if __name__ == "__main__":
    test_numbers = [7, 14, 17, 27, 28, 10, 15]
    for num in test_numbers:
        print(f"Is {num} a Buzz Number? {is_buzz_number(num)}")
