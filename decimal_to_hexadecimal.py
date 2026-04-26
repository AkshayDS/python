# Problem: Convert Decimal to Hexadecimal
# Description: Write a function `decimal_to_hex(n)` that converts a decimal number to its hexadecimal representation.

def decimal_to_hex(n):
    if n == 0:
        return "0x0"
    
    hex_chars = "0123456789ABCDEF"
    hex_result = ""
    
    # Handle negative numbers
    is_negative = False
    if n < 0:
        is_negative = True
        n = abs(n)
        
    while n > 0:
        remainder = n % 16
        hex_result = hex_chars[remainder] + hex_result
        n //= 16
        
    return ("-" if is_negative else "") + "0x" + hex_result

# Basic Example
if __name__ == "__main__":
    num = 255
    print(f"Decimal {num} in Hexadecimal: {decimal_to_hex(num)}")

    num2 = 4096
    print(f"Decimal {num2} in Hexadecimal: {decimal_to_hex(num2)}")
    
    num3 = -31
    print(f"Decimal {num3} in Hexadecimal: {decimal_to_hex(num3)}")
