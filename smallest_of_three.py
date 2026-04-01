# Problem: Find the Smallest of Three Numbers
# Description: Write a function `find_smallest(a, b, c)` that returns the smallest of three numbers.

def find_smallest(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

# Basic Example
if __name__ == "__main__":
    num1 = 12
    num2 = 45
    num3 = 32
    smallest = find_smallest(num1, num2, num3)
    print(f"The smallest of {num1}, {num2}, and {num3} is: {smallest}")

    # Another example
    print("Smallest of 5, 10, 3 is:", find_smallest(5, 10, 3))
