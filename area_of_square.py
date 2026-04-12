# Problem: Calculate Area of a Square
# Description: Write a function `area_of_square(side)` that returns the area of a square given its side length.
# Formula: Area = side * side

def area_of_square(side):
    if side < 0:
        return "Side length cannot be negative"
    return side * side

# Basic Example
if __name__ == "__main__":
    s1 = 5
    area = area_of_square(s1)
    print(f"The area of a square with side {s1} is: {area}")

    # Another example
    s2 = 12
    print(f"Side: {s2} -> Area: {area_of_square(s2)}")
