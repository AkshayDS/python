"""
Script to convert temperature between Celsius and Fahrenheit.
Demonstrates basic arithmetic operations.
Formula: F = C * 9/5 + 32
"""

def celsius_to_fahrenheit(c: float) -> float:
    """
    Converts Celsius to Fahrenheit.
    """
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f: float) -> float:
    """
    Converts Fahrenheit to Celsius.
    """
    return (f - 32) * 5/9
