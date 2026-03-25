# Problem: Absolute Value
# Description: Write a function `absolute_value(n)` that returns the absolute value of a number.

def absolute_value(n):
    if n < 0:
        return -n
    return n

# Basic Example
if __name__ == "__main__":
    num1 = -7
    result1 = absolute_value(num1)
    print(f"The absolute value of {num1} is: {result1}")

    # Another example
    num2 = 10
    print(f"The absolute value of {num2} is: {absolute_value(num2)}")
