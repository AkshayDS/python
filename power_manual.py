# Problem: Power of a Number
# Description: Write a function `power(base, exp)` that returns base raised to the power of exp.

def power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

# Basic Example
if __name__ == "__main__":
    base = 2
    exp = 10
    result = power(base, exp)
    print(f"{base} raised to the power of {exp} is: {result}")

    # Another example
    print(f"3 raised to the power of 4 is: {power(3, 4)}")
