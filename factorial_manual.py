"""
Script to calculate the factorial of a number without using Python's built-in `math.factorial()`.
Factorial of n (denoted as n!) is the product of all positive integers less than or equal to n.
Example: 5! = 5 * 4 * 3 * 2 * 1 = 120
"""

def factorial_iterative(n: int) -> int:
    """
    Calculates factorial using a loop.
    Generally preferred for large numbers in Python to avoid hitting the recursion depth limit.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
        
    result = 1
    for i in range(2, n + 1):
        result *= i
        
    return result


def factorial_recursive(n: int) -> int:
    """
    Calculates factorial using recursion.
    Elegant and mathematical, but can cause a RecursionError for extremely large n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
        
    return n * factorial_recursive(n - 1)


# --- Test Executions ---
if __name__ == "__main__":
    print("--- Factorial Check (No Built-ins) ---")
    
    test_numbers = [0, 5, 10]
    
    for num in test_numbers:
        print(f"\nNumber: {num}")
        print(f"  -> Iterative: {factorial_iterative(num)}")
        print(f"  -> Recursive: {factorial_recursive(num)}")
