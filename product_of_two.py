# Problem: Product of Two Numbers
# Description: Write a function `multiply(a, b)` that returns the product of two numbers.

def multiply(a, b):
    return a * b

# Basic Example
if __name__ == "__main__":
    num1 = 6
    num2 = 7
    result = multiply(num1, num2)
    print(f"The product of {num1} and {num2} is: {result}")

    # Another example
    print(f"Product of 12 and 5 is: {multiply(12, 5)}")
