# Problem: Cube of a Number
# Description: Write a function `cube(n)` that returns the cube of a given number.

def cube(n):
    return n ** 3

# Basic Example
if __name__ == "__main__":
    num1 = 3
    result1 = cube(num1)
    print(f"The cube of {num1} is: {result1}")

    # Another example
    num2 = -2
    print(f"The cube of {num2} is: {cube(num2)}")
