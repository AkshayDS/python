"""
Script to check if a number is a Disarium Number.
A Disarium number is a number in which the sum of the digits raised to the 
power of their respective positions is equal to the number itself.

Example: 175 is a Disarium number.
1^1 + 7^2 + 5^3 = 1 + 49 + 125 = 175
"""

def is_disarium_number(n: int) -> bool:
    """
    Returns True if n is a Disarium number, otherwise False.
    """
    if n < 0:
        return False
        
    # Convert to string to easily iterate over digits and positions
    s = str(n)
    temp_sum = 0
    
    for i in range(len(s)):
        digit = int(s[i])
        # Position is i + 1 (1-based)
        temp_sum += digit ** (i + 1)
        
    return temp_sum == n

if __name__ == "__main__":
    test_numbers = [175, 89, 135, 80, 1, 518]
    for num in test_numbers:
        print(f"Is {num} a Disarium Number? {is_disarium_number(num)}")
