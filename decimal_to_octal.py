# Problem: Convert Decimal to Octal
# Description: Write a function `decimal_to_octal(n)` that converts a decimal number to its octal representation.

def decimal_to_octal(n):
    if n == 0:
        return "0o0"
    
    octal_result = ""
    
    # Handle negative numbers
    is_negative = False
    if n < 0:
        is_negative = True
        n = abs(n)
        
    while n > 0:
        remainder = n % 8
        octal_result = str(remainder) + octal_result
        n //= 8
        
    return ("-" if is_negative else "") + "0o" + octal_result

# Basic Example
if __name__ == "__main__":
    num1 = 64
    print(f"Decimal {num1} in Octal: {decimal_to_octal(num1)}")

    num2 = 125
    print(f"Decimal {num2} in Octal: {decimal_to_octal(num2)}")
    
    num3 = -35
    print(f"Decimal {num3} in Octal: {decimal_to_octal(num3)}")
