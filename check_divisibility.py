# Problem: Check Divisibility
# Description: Write a function `is_divisible(a, b)` that checks if a is divisible by b.

def is_divisible(a, b):
    if b == 0:
        return False
    return a % b == 0

# Basic Example
if __name__ == "__main__":
    num1 = 10
    num2 = 5
    result = is_divisible(num1, num2)
    print(f"Is {num1} divisible by {num2}? {result}")

    # Another example
    print(f"Is 7 divisible by 3? {is_divisible(7, 3)}")
