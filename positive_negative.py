"""
Script to check if a number is positive, negative, or zero.
Demonstrates basic if-elif-else Conditional logic.
"""

def check_number(n: int) -> str:
    """
    Checks if a number is positive, negative, or zero.
    """
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

def check_number_short(n: int) -> str:
    """
    Checks if a number is positive, negative, or zero using a single expression.
    """
    return "Positive" if n > 0 else "Negative" if n < 0 else "Zero"
