"""
Script to check if a number is a Duck Number.
A Duck number is a number which has zero present in it, but not at the beginning.

Example: 3210 is a Duck number.
Example: 0321 is NOT a Duck number.
Example: 1023 is a Duck number.
"""

def is_duck_number(n: str) -> bool:
    """
    Returns True if the string representation of n is a Duck number.
    """
    if not n:
        return False
        
    # Standard definition usually considers the number as a string input
    # or assumes no leading zeros for integers.
    # If the first character is '0', it's not a duck number.
    if n[0] == '0':
        return False
        
    # Check if '0' exists in the rest of the number
    return '0' in n

if __name__ == "__main__":
    test_cases = ["3210", "1023", "0321", "123", "100", "0"]
    for test in test_cases:
        print(f"Is '{test}' a Duck Number? {is_duck_number(test)}")
