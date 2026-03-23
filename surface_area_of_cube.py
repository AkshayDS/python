# Problem: Surface Area of a Cube
# Description: Write a function `surface_area_cube(side)` that returns the surface area of a cube.
# Formula: Surface Area = 6 * side^2

def surface_area_cube(side):
    return 6 * (side ** 2)

# Basic Example
if __name__ == "__main__":
    side_length = 4
    area = surface_area_cube(side_length)
    print(f"The surface area of a cube with side length {side_length} is: {area}")

    # Another example
    side2 = 5.5
    print(f"Side Length: {side2} -> Surface Area: {surface_area_cube(side2)}")
