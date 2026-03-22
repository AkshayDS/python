# Problem: Perimeter of a Rectangle
# Description: Write a function `calculate_perimeter(length, width)` that returns the perimeter of a rectangle.
# Formula: Perimeter = 2 * (length + width)

def calculate_perimeter(length, width):
    return 2 * (length + width)

# Basic Example
if __name__ == "__main__":
    length = 5
    width = 3
    perimeter = calculate_perimeter(length, width)
    print(f"The perimeter of a rectangle with length {length} and width {width} is: {perimeter}")

    # Another example
    len2 = 10
    wid2 = 7
    print(f"Length: {len2}, Width: {wid2} -> Perimeter: {calculate_perimeter(len2, wid2)}")
