# Problem: Convert Celsius to Kelvin
# Description: Write a function `celsius_to_kelvin(celsius)` that converts temperature from Celsius to Kelvin.
# Formula: Kelvin = Celsius + 273.15

def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Basic Example
if __name__ == "__main__":
    c1 = 25
    k1 = celsius_to_kelvin(c1)
    print(f"{c1} degrees Celsius is equal to {k1} Kelvin")

    # Another example
    c2 = 0
    print(f"{c2} degrees Celsius is equal to {celsius_to_kelvin(c2)} Kelvin")
