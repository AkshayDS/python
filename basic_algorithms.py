"""
A collection of simple Python algorithms and utility functions.
These demonstrate basic syntax, loops, and built-in methods.
"""

def add_numbers(a: int, b: int) -> int:
    """Returns the sum of two numbers."""
    return a + b

def calculate_factorial(n: int) -> int:
    """Calculates the factorial of a number iteratively."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome ignoring case and spaces."""
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

def generate_fibonacci(n: int) -> list:
    """Generates the first n numbers in the Fibonacci sequence."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def find_min_max(numbers: list) -> tuple:
    """Finds the minimum and maximum numbers in a list."""
    if not numbers:
        return None, None
    return min(numbers), max(numbers)

# --- Test Executions ---
if __name__ == "__main__":
    print("--- Simple Python Algorithms ---")
    print(f"1. Addition: 15 + 27 = {add_numbers(15, 27)}")
    
    print(f"\n2. Factorial: 5! = {calculate_factorial(5)}")
    
    test_str = "A man a plan a canal Panama"
    print(f"\n3. Palindrome Check: '{test_str}' -> {is_palindrome(test_str)}")
    
    print(f"\n4. Fibonacci (First 10 terms): {generate_fibonacci(10)}")
    
    nums = [45, 12, 78, 4, 99, 23, 11]
    min_val, max_val = find_min_max(nums)
    print(f"\n5. Min/Max of {nums}: Min={min_val}, Max={max_val}")
