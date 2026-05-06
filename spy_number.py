"""
Script to check if a number is a Spy Number.
A Spy number is a number where the sum of its digits is equal to the product 
of its digits.

Example: 1124 is a Spy number.
Sum: 1 + 1 + 2 + 4 = 8
Product: 1 * 1 * 2 * 4 = 8
"""

def is_spy_number(n: int) -> bool:
    """
    Returns True if n is a spy number, otherwise False.
    """
    if n < 0:
        return False
        
    temp = n
    digit_sum = 0
    digit_product = 1
    
    # Process each digit
    if n == 0:
        return True # 0: sum=0, product=0 (usually considered)
        
    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        digit_product *= digit
        temp //= 10
        
    return digit_sum == digit_product

if __name__ == "__main__":
    test_numbers = [1124, 123, 22, 132, 0, 7]
    for num in test_numbers:
        print(f"Is {num} a Spy Number? {is_spy_number(num)}")
