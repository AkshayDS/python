# Problem: Area of a Triangle
# Description: Write a function `area_of_triangle(base, height)` that returns the area of a triangle.

def area_of_triangle(base, height):
    return 0.5 * base * height

# Basic Example
if __name__ == "__main__":
    base = 10
    height = 5
    area = area_of_triangle(base, height)
    print(f"The area of the triangle with base {base} and height {height} is: {area}")

    # Another example
    print("Area of triangle with base 7 and height 4 is:", area_of_triangle(7, 4))
