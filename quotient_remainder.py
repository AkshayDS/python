# Problem: Quotient and Remainder
# Description: Write a function `divide(a, b)` that returns the quotient and remainder.

def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

# Basic Example
if __name__ == "__main__":
    num1 = 17
    num2 = 5
    q, r = divide(num1, num2)
    print(f"{num1} divided by {num2} gives quotient: {q} and remainder: {r}")

    # Another example
    q2, r2 = divide(25, 4)
    print(f"25 divided by 4 gives quotient: {q2} and remainder: {r2}")
