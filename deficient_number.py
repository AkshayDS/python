"""
Script to check if a number is a Deficient Number.
A deficient number is a number for which the sum of its proper divisors 
(excluding the number itself) is less than the number itself.

Example: 8 is a deficient number.
Proper divisors: 1, 2, 4
Sum: 1 + 2 + 4 = 7
7 < 8
"""

def is_deficient_number(n: int) -> bool:
    """
    Returns True if n is a deficient number, otherwise False.
    """
    if n <= 0:
        return False
        
    # Calculate the sum of its proper divisors
    divisor_sum = 0
    # A divisor cannot be more than n/2 (excluding n itself)
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            divisor_sum += i
            
    return divisor_sum < n

if __name__ == "__main__":
    test_numbers = [8, 10, 15, 21, 12, 18]
    for num in test_numbers:
        print(f"Is {num} a Deficient Number? {is_deficient_number(num)}")
