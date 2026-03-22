# Problem: Square of a Number
# Description: Write a function `square(n)` that returns the square of a given number.

def square(n):
    return n * n

# Basic Example
if __name__ == "__main__":
    num1 = 5
    result1 = square(num1)
    print(f"The square of {num1} is: {result1}")

    # Another example
    num2 = -4
    print(f"The square of {num2} is: {square(num2)}")
