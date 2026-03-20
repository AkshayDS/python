# Problem: Find the Largest of Three Numbers
# Description: Write a function `find_largest(a, b, c)` that returns the largest of three numbers.

def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Basic Example
if __name__ == "__main__":
    num1 = 12
    num2 = 45
    num3 = 32
    largest = find_largest(num1, num2, num3)
    print(f"The largest of {num1}, {num2}, and {num3} is: {largest}")

    # Another example
    print("Largest of 5, 10, 3 is:", find_largest(5, 10, 3))
