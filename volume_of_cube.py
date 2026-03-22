# Problem: Volume of a Cube
# Description: Write a function `cube_volume(side)` that returns the volume of a cube.
# Formula: Volume = side ** 3

def cube_volume(side):
    return side ** 3

# Basic Example
if __name__ == "__main__":
    side_length = 4
    volume = cube_volume(side_length)
    print(f"The volume of a cube with side length {side_length} is: {volume}")

    # Another example
    side2 = 5.5
    print(f"Side Length: {side2} -> Volume: {cube_volume(side2)}")
