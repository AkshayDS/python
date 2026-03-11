"""
Script to solve the classic 'FizzBuzz' programming interview challenge.
Demonstrates looping from 1 to N and using the modulo operator for condition checking.
"""

def generate_fizz_buzz(n: int) -> list:
    """
    Returns a list of string representations of numbers from 1 to n.
    - Multiples of 3 are replaced with "Fizz"
    - Multiples of 5 are replaced with "Buzz"
    - Multiples of both 3 and 5 are replaced with "FizzBuzz"
    """
    result = []
    
    for i in range(1, n + 1):
        # Check divisibility by both 3 and 5 first
        # (This is the same as checking divisibility by their product, 15)
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        # Then check divisibility by 3
        elif i % 3 == 0:
            result.append("Fizz")
        # Then check divisibility by 5
        elif i % 5 == 0:
            result.append("Buzz")
        # Otherwise, just append the number as a string
        else:
            result.append(str(i))
            
    return result
