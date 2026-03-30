# Problem: Circumference of a Circle
# Description: Write a function `circumference(radius)` that returns the circumference of a circle.
# Formula: Circumference = 2 * pi * radius

import math

def circumference(radius):
    return 2 * math.pi * radius

# Basic Example
if __name__ == "__main__":
    r1 = 7
    result1 = circumference(r1)
    print(f"The circumference of a circle with radius {r1} is: {result1:.2f}")

    # Another example
    r2 = 3.5
    print(f"Radius: {r2} -> Circumference: {circumference(r2):.2f}")
