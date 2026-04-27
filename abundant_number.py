"""
Script to check if a number is an Abundant Number.
An abundant number is a number for which the sum of its proper divisors 
(excluding the number itself) is greater than the number itself.

Example: 12 is an abundant number.
Proper divisors: 1, 2, 3, 4, 6
Sum: 1 + 2 + 3 + 4 + 6 = 16
16 > 12
"""

def is_abundant_number(n: int) -> bool:
    """
    Returns True if n is an abundant number, otherwise False.
    """
    if n <= 0:
        return False
        
    # Calculate the sum of its proper divisors
    divisor_sum = 0
    # A divisor cannot be more than n/2 (excluding n itself)
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            divisor_sum += i
            
    return divisor_sum > n

if __name__ == "__main__":
    test_numbers = [12, 18, 20, 24, 30, 8, 10, 15]
    for num in test_numbers:
        print(f"Is {num} an Abundant Number? {is_abundant_number(num)}")
