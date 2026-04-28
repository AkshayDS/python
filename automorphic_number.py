"""
Script to check if a number is an Automorphic Number.
An automorphic number is a number whose square ends in the same digits as the number itself.

Example: 25 is an automorphic number.
25^2 = 625 (ends in 25)
"""

def is_automorphic_number(n: int) -> bool:
    """
    Returns True if n is an automorphic number, otherwise False.
    """
    if n < 0:
        return False
        
    sq_n = n * n
    
    # Convert both to strings and check if square ends with the number
    return str(sq_n).endswith(str(n))

def is_automorphic_number_math(n: int) -> bool:
    """
    Alternative mathematical approach without using strings.
    """
    if n < 0:
        return False
        
    sq_n = n * n
    temp = n
    
    while temp > 0:
        # Compare last digits
        if temp % 10 != sq_n % 10:
            return False
        temp //= 10
        sq_n //= 10
        
    return True

if __name__ == "__main__":
    test_numbers = [5, 6, 25, 76, 376, 7, 10, 11]
    print("Using string method:")
    for num in test_numbers:
        print(f"Is {num} an Automorphic Number? {is_automorphic_number(num)}")
        
    print("\nUsing math method:")
    for num in test_numbers:
        print(f"Is {num} an Automorphic Number? {is_automorphic_number_math(num)}")
