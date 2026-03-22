# Problem: Area of a Rectangle
# Description: Write a function `calculate_area(length, width)` that returns the area of a rectangle.
# Formula: Area = length * width

def calculate_area(length, width):
    return length * width

# Basic Example
if __name__ == "__main__":
    length = 5
    width = 3
    area = calculate_area(length, width)
    print(f"The area of a rectangle with length {length} and width {width} is: {area}")

    # Another example
    len2 = 10
    wid2 = 7
    print(f"Length: {len2}, Width: {wid2} -> Area: {calculate_area(len2, wid2)}")
