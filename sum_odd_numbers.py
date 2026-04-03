# Problem: Sum of Odd Numbers in a Range
# Description: Write a function `sum_odd(n)` that returns the sum of all odd numbers from 1 to n.

def sum_odd(n):
    total = 0
    for i in range(1, n + 1, 2):
        total += i
    return total

# Basic Example
if __name__ == "__main__":
    num1 = 10
    result1 = sum_odd(num1)
    print(f"Sum of odd numbers from 1 to {num1} is: {result1}")

    # Another example
    num2 = 20
    print(f"Sum of odd numbers from 1 to {num2} is: {sum_odd(num2)}")
