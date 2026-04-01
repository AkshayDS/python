# Problem: Sum of Even Numbers in a Range
# Description: Write a function `sum_even(n)` that returns the sum of all even numbers from 1 to n.

def sum_even(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total

# Basic Example
if __name__ == "__main__":
    num1 = 10
    result1 = sum_even(num1)
    print(f"Sum of even numbers from 1 to {num1} is: {result1}")

    # Another example
    num2 = 20
    print(f"Sum of even numbers from 1 to {num2} is: {sum_even(num2)}")
