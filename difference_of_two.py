# Problem: Difference of Two Numbers
# Description: Write a function `difference(a, b)` that returns the absolute difference of two numbers.

def difference(a, b):
    if a > b:
        return a - b
    return b - a

# Basic Example
if __name__ == "__main__":
    num1 = 15
    num2 = 8
    result = difference(num1, num2)
    print(f"The difference between {num1} and {num2} is: {result}")

    # Another example
    print(f"Difference of 3 and 10 is: {difference(3, 10)}")
