# Problem: Celsius to Fahrenheit Converter
# Description: Write a function `celsius_to_fahrenheit(c)` that converts Celsius to Fahrenheit.

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Basic Example
if __name__ == "__main__":
    celsius = 25
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")

    # Another example
    celsius2 = 0
    print(f"{celsius2} degrees Celsius is equal to {celsius_to_fahrenheit(celsius2)} degrees Fahrenheit")
