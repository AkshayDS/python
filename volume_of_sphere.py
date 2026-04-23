# Problem: Calculate Volume of a Sphere
# Description: Write a function `volume_of_sphere(radius)` that returns the volume of a sphere.
# Formula: Volume = (4/3) * pi * radius^3

import math

def volume_of_sphere(radius):
    if radius < 0:
        return "Radius must be non-negative"
    return (4/3) * math.pi * (radius ** 3)

# Basic Example
if __name__ == "__main__":
    r = 3
    volume = volume_of_sphere(r)
    print(f"The volume of a sphere with radius {r} is: {volume:.2f}")

    # Another example
    r2 = 5
    print(f"Radius: {r2} -> Volume: {volume_of_sphere(r2):.2f}")
