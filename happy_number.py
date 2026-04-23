"""
Script to check if a number is a Happy Number.
A happy number is defined by the following process: Starting with any positive 
integer, replace the number by the sum of the squares of its digits, and repeat 
the process until the number equals 1 (where it will stay), or it loops 
endlessly in a cycle which does not include 1. 

Example: 19 is a happy number.
1^2 + 9^2 = 1 + 81 = 82
8^2 + 2^2 = 64 + 4 = 68
6^2 + 8^2 = 36 + 64 = 100
1^2 + 0^2 + 0^2 = 1 + 0 + 0 = 1
"""

def is_happy_number(n: int) -> bool:
    """
    Returns True if n is a happy number, otherwise False.
    """
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        # Sum of squares of its digits
        temp_sum = 0
        while n > 0:
            digit = n % 10
            temp_sum += digit * digit
            n //= 10
        n = temp_sum
    return n == 1

if __name__ == "__main__":
    test_numbers = [19, 7, 2, 4, 1, 100]
    for num in test_numbers:
        print(f"Is {num} a Happy Number? {is_happy_number(num)}")
