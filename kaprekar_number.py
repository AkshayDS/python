"""
Script to check if a number is a Kaprekar Number.
A Kaprekar number is a number whose square can be split into two parts 
which add up to the original number.

Example: 45 is a Kaprekar number.
45^2 = 2025
Split 2025 into 20 and 25
20 + 25 = 45
"""

def is_kaprekar_number(n: int) -> bool:
    """
    Returns True if n is a Kaprekar number, otherwise False.
    """
    if n == 1:
        return True
    
    sq_n = n * n
    s_sq = str(sq_n)
    d = len(s_sq)
    
    # Try all possible splits of the squared number
    for i in range(1, d):
        left_part = s_sq[:i]
        right_part = s_sq[i:]
        
        l = int(left_part) if left_part else 0
        r = int(right_part) if right_part else 0
        
        # The right part 'r' should be positive according to standard Kaprekar definition
        if r > 0 and l + r == n:
            return True
            
    return False

if __name__ == "__main__":
    test_numbers = [1, 9, 45, 55, 99, 297, 703, 10]
    for num in test_numbers:
        print(f"Is {num} a Kaprekar Number? {is_kaprekar_number(num)}")
