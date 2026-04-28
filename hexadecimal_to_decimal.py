# Problem: Convert Hexadecimal to Decimal
# Description: Write a function `hex_to_decimal(hex_str)` that converts a hexadecimal string to a decimal integer.

def hex_to_decimal(hex_str):
    hex_str = hex_str.upper()
    if hex_str.startswith("0X"):
        hex_str = hex_str[2:]
        
    if hex_str.startswith("-0X"):
        return -hex_to_decimal(hex_str[3:])
    elif hex_str.startswith("-"):
        return -hex_to_decimal(hex_str[1:])
        
    hex_chars = "0123456789ABCDEF"
    decimal_result = 0
    
    for char in hex_str:
        if char not in hex_chars:
            return "Invalid hexadecimal string"
        decimal_result = decimal_result * 16 + hex_chars.index(char)
        
    return decimal_result

# Basic Example
if __name__ == "__main__":
    hex1 = "FF"
    print(f"Hexadecimal '{hex1}' in Decimal: {hex_to_decimal(hex1)}")

    hex2 = "0x1000"
    print(f"Hexadecimal '{hex2}' in Decimal: {hex_to_decimal(hex2)}")
    
    hex3 = "-1F"
    print(f"Hexadecimal '{hex3}' in Decimal: {hex_to_decimal(hex3)}")
