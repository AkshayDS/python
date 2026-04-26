"""
Script to check if a number is a Pronic Number.
A pronic number is a number which is the product of two consecutive integers, 
that is, a number of the form n(n + 1).

Example: 12 is a pronic number because 3 * 4 = 12.
"""

def is_pronic_number(num: int) -> bool:
    """
    Returns True if num is a Pronic number, otherwise False.
    """
    if num < 0:
        return False
        
    # Check if any integer i multiplied by (i+1) equals num
    # i only needs to go up to the square root of num
    for i in range(int(num**0.5) + 1):
        if i * (i + 1) == num:
            return True
            
    return False

if __name__ == "__main__":
    test_numbers = [0, 2, 6, 12, 20, 30, 42, 5, 10]
    for num in test_numbers:
        print(f"Is {num} a Pronic Number? {is_pronic_number(num)}")
