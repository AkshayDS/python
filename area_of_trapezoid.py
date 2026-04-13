# Problem: Calculate Area of a Trapezoid
# Description: Write a function `area_of_trapezoid(a, b, height)` that returns the area of a trapezoid.
# Formula: Area = ((a + b) / 2) * height

def area_of_trapezoid(a, b, height):
    if a < 0 or b < 0 or height < 0:
        return "Lengths and height must be non-negative"
    return ((a + b) / 2) * height

# Basic Example
if __name__ == "__main__":
    base1 = 8
    base2 = 10
    h = 5
    area = area_of_trapezoid(base1, base2, h)
    print(f"The area of a trapezoid with bases {base1} and {base2} and height {h} is: {area}")

    # Another example
    b1 = 12
    b2 = 14
    h2 = 7
    print(f"Bases: {b1}, {b2}, Height: {h2} -> Area: {area_of_trapezoid(b1, b2, h2)}")
