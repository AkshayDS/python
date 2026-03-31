# Problem: Count Digits in a Number
# Description: Write a function `count_digits(n)` that returns the number of digits in a given number.

def count_digits(n):
    if n == 0:
        return 1
    count = 0
    n = abs(n)
    while n > 0:
        count += 1
        n //= 10
    return count

# Basic Example
if __name__ == "__main__":
    num1 = 12345
    result1 = count_digits(num1)
    print(f"The number {num1} has {result1} digits")

    # Another example
    num2 = -987
    print(f"The number {num2} has {count_digits(num2)} digits")
