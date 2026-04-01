"""
Script to convert a decimal number to its binary, octal, and hexadecimal equivalents.
Demonstrates number base conversion using manual division and built-in functions.
"""

def decimal_to_binary_manual(n: int) -> str:
    """
    Converts decimal to binary using manual division.
    """
    if n == 0:
        return "0"
    result = ""
    num = abs(n)
    while num > 0:
        result = str(num % 2) + result
        num //= 2
    return "-" + result if n < 0 else result

def decimal_to_octal_manual(n: int) -> str:
    """
    Converts decimal to octal using manual division.
    """
    if n == 0:
        return "0"
    result = ""
    num = abs(n)
    while num > 0:
        result = str(num % 8) + result
        num //= 8
    return "-" + result if n < 0 else result

def convert_all(n: int) -> dict:
    """
    Converts decimal to binary, octal, and hexadecimal using built-in functions.
    """
    return {
        "binary": bin(n),
        "octal": oct(n),
        "hexadecimal": hex(n)
    }
