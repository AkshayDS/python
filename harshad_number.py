"""
Script to check if a number is a Harshad (or Niven) Number.
A Harshad number is an integer that is divisible by the sum of its digits.

Example: 18 is a Harshad number.
1 + 8 = 9
18 / 9 = 2 (No remainder)
"""

def is_harshad_number(n: int) -> bool:
    """
    Returns True if n is a Harshad number, otherwise False.
    """
    if n <= 0:
        return False
        
    # Calculate the sum of its digits
    temp = n
    digit_sum = 0
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
        
    # Check if the number is divisible by the digit sum
    return n % digit_sum == 0

if __name__ == "__main__":
    test_numbers = [1, 18, 21, 20, 153, 5, 27]
    for num in test_numbers:
        print(f"Is {num} a Harshad Number? {is_harshad_number(num)}")
