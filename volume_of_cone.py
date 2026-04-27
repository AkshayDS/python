# Problem: Calculate Volume of a Cone
# Description: Write a function `volume_of_cone(radius, height)` that returns the volume of a cone.
# Formula: Volume = (1/3) * pi * radius^2 * height

import math

def volume_of_cone(radius, height):
    if radius < 0 or height < 0:
        return "Radius and height must be non-negative"
    return (1/3) * math.pi * (radius ** 2) * height

# Basic Example
if __name__ == "__main__":
    r = 3
    h = 7
    volume = volume_of_cone(r, h)
    print(f"The volume of a cone with radius {r} and height {h} is: {volume:.2f}")

    # Another example
    r2 = 5
    h2 = 12
    print(f"Radius: {r2}, Height: {h2} -> Volume: {volume_of_cone(r2, h2):.2f}")
