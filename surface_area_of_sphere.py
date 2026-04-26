# Problem: Calculate Surface Area of a Sphere
# Description: Write a function `surface_area_of_sphere(radius)` that returns the surface area of a sphere.
# Formula: Surface Area = 4 * pi * radius^2

import math

def surface_area_of_sphere(radius):
    if radius < 0:
        return "Radius must be non-negative"
    return 4 * math.pi * (radius ** 2)

# Basic Example
if __name__ == "__main__":
    r = 3
    area = surface_area_of_sphere(r)
    print(f"The surface area of a sphere with radius {r} is: {area:.2f}")

    # Another example
    r2 = 5.5
    print(f"Radius: {r2} -> Surface Area: {surface_area_of_sphere(r2):.2f}")
