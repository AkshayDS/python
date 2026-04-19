# Problem: Convert Liters to Milliliters
# Description: Write a function `liters_to_ml(liters)` that converts liters to milliliters.
# Formula: 1 liter = 1000 milliliters

def liters_to_ml(liters):
    if liters < 0:
        return "Volume cannot be negative"
    return liters * 1000

# Basic Example
if __name__ == "__main__":
    l1 = 5
    ml1 = liters_to_ml(l1)
    print(f"{l1} liters is equal to {ml1} milliliters")

    # Another example
    l2 = 2.5
    print(f"{l2} liters is equal to {liters_to_ml(l2)} milliliters")
