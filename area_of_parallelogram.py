# Problem: Calculate Area of a Parallelogram
# Description: Write a function `area_of_parallelogram(base, height)` that returns the area of a parallelogram.
# Formula: Area = base * height

def area_of_parallelogram(base, height):
    if base < 0 or height < 0:
        return "Base and height must be non-negative"
    return base * height

# Basic Example
if __name__ == "__main__":
    b1 = 10
    h1 = 5
    area = area_of_parallelogram(b1, h1)
    print(f"The area of a parallelogram with base {b1} and height {h1} is: {area}")

    # Another example
    b2 = 15
    h2 = 8
    print(f"Base: {b2}, Height: {h2} -> Area: {area_of_parallelogram(b2, h2)}")
