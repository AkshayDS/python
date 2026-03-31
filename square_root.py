# Problem: Square Root of a Number
# Description: Write a function `square_root(n)` that returns the square root of a number.

import math

def square_root(n):
    return math.sqrt(n)

# Basic Example
if __name__ == "__main__":
    num1 = 25
    result1 = square_root(num1)
    print(f"The square root of {num1} is: {result1}")

    # Another example
    num2 = 144
    print(f"The square root of {num2} is: {square_root(num2)}")
