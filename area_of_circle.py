"""
Script to calculate the area and circumference of a circle.
Demonstrates the use of constants (pi) and basic math operations.
Formula: 
Area = pi * r^2
Circumference = 2 * pi * r
"""

import math

def calculate_area(radius: float) -> float:
    """
    Calculates the area of a circle given its radius.
    """
    return math.pi * (radius ** 2)

def calculate_circumference(radius: float) -> float:
    """
    Calculates the circumference of a circle given its radius.
    """
    return 2 * math.pi * radius
