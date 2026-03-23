# Problem: Meters to Centimeters Converter
# Description: Write a function `meters_to_cm(meters)` that converts meters to centimeters.
# Formula: 1 meter = 100 centimeters.

def meters_to_cm(meters):
    return meters * 100

# Basic Example
if __name__ == "__main__":
    meters1 = 5
    cm1 = meters_to_cm(meters1)
    print(f"{meters1} meters is equal to {cm1} centimeters")

    # Another example
    meters2 = 1.5
    print(f"{meters2} meters is equal to {meters_to_cm(meters2)} centimeters")
