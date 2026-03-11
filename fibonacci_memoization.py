"""
Script to calculate the nth Fibonacci number using Dynamic Programming (Memoization).
This optimizes the incredibly slow O(2^n) standard recursive approach 
down to a blazing fast O(n) time complexity by caching previously calculated results.
"""

def fibonacci_memoized(n: int, memo: dict = None) -> int:
    """
    Calculates the nth Fibonacci number recursively using a dictionary cache (memo).
    """
    # Initialize the memoization dictionary on the first call
    if memo is None:
        memo = {}
        
    # Check if we have already computed this value
    if n in memo:
        return memo[n]
        
    # Base cases for Fibonacci sequence
    if n <= 0:
        return 0
    if n == 1:
        return 1
        
    # Recursively calculate the nth Fibonacci number
    # Store the result in our memo dictionary before returning it
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    
    return memo[n]
