# Problem: Calculate Surface Area of a Cone
# Description: Write a function `surface_area_of_cone(radius, height)` that returns the total surface area of a cone.
# Formula: Surface Area = pi * r * (r + sqrt(r^2 + h^2))

import math

def surface_area_of_cone(radius, height):
    if radius < 0 or height < 0:
        return "Radius and height must be non-negative"
    slant_height = math.sqrt(radius**2 + height**2)
    return math.pi * radius * (radius + slant_height)

# Basic Example
if __name__ == "__main__":
    r = 3
    h = 4
    area = surface_area_of_cone(r, h)
    print(f"The surface area of a cone with radius {r} and height {h} is: {area:.2f}")

    # Another example
    r2 = 5
    h2 = 12
    print(f"Radius: {r2}, Height: {h2} -> Surface Area: {surface_area_of_cone(r2, h2):.2f}")
