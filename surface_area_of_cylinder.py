# Problem: Calculate Surface Area of a Cylinder
# Description: Write a function `surface_area_of_cylinder(radius, height)` that returns the total surface area of a cylinder.
# Formula: Surface Area = 2 * pi * radius * (radius + height)

import math

def surface_area_of_cylinder(radius, height):
    if radius < 0 or height < 0:
        return "Radius and height must be non-negative"
    return 2 * math.pi * radius * (radius + height)

# Basic Example
if __name__ == "__main__":
    r = 3
    h = 7
    area = surface_area_of_cylinder(r, h)
    print(f"The surface area of a cylinder with radius {r} and height {h} is: {area:.2f}")

    # Another example
    r2 = 2.5
    h2 = 10
    print(f"Radius: {r2}, Height: {h2} -> Surface Area: {surface_area_of_cylinder(r2, h2):.2f}")
