# Problem: Calculate Volume of a Cylinder
# Description: Write a function `volume_of_cylinder(radius, height)` that returns the volume of a cylinder.
# Formula: Volume = pi * radius^2 * height

import math

def volume_of_cylinder(radius, height):
    if radius < 0 or height < 0:
        return "Radius and height must be non-negative"
    return math.pi * (radius ** 2) * height

# Basic Example
if __name__ == "__main__":
    r = 3
    h = 5
    volume = volume_of_cylinder(r, h)
    print(f"The volume of a cylinder with radius {r} and height {h} is: {volume:.2f}")

    # Another example
    r2 = 2.5
    h2 = 10
    print(f"Radius: {r2}, Height: {h2} -> Volume: {volume_of_cylinder(r2, h2):.2f}")
