"""
Script to convert a decimal (base-10) integer to a binary (base-2) string.
Demonstrates the iterative method of successive division by 2.
"""

def decimal_to_binary(n: int) -> str:
    """
    Converts a decimal integer to a binary string representation.
    """
    if n == 0:
        return "0"
        
    binary = ""
    num = abs(n)
    
    while num > 0:
        # Get the remainder (either 0 or 1)
        remainder = num % 2
        # Prepend the remainder to our binary string
        binary = str(remainder) + binary
        # Divide the number by 2 (integer division)
        num = num // 2
        
    return "-" + binary if n < 0 else binary

def decimal_to_binary_built_in(n: int) -> str:
    """
    Converts a decimal integer to a binary string using Python's built-in bin() function.
    Returns the string without the '0b' prefix.
    """
    if n < 0:
        return "-" + bin(n)[3:]
    return bin(n)[2:]
