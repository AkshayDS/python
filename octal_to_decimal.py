# Problem: Convert Octal to Decimal
# Description: Write a function `octal_to_decimal(octal_str)` that converts an octal string to a decimal integer.

def octal_to_decimal(octal_str):
    if octal_str.startswith("0o") or octal_str.startswith("0O"):
        octal_str = octal_str[2:]
        
    if octal_str.startswith("-0o") or octal_str.startswith("-0O"):
        return -octal_to_decimal(octal_str[3:])
    elif octal_str.startswith("-"):
        return -octal_to_decimal(octal_str[1:])
        
    octal_chars = "01234567"
    decimal_result = 0
    
    for char in octal_str:
        if char not in octal_chars:
            return "Invalid octal string"
        decimal_result = decimal_result * 8 + octal_chars.index(char)
        
    return decimal_result

# Basic Example
if __name__ == "__main__":
    octal1 = "77"
    print(f"Octal '{octal1}' in Decimal: {octal_to_decimal(octal1)}")

    octal2 = "0o100"
    print(f"Octal '{octal2}' in Decimal: {octal_to_decimal(octal2)}")
    
    octal3 = "-12"
    print(f"Octal '{octal3}' in Decimal: {octal_to_decimal(octal3)}")
