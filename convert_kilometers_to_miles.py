# Problem: Convert Kilometers to Miles
# Description: Write a function `km_to_miles(km)` that converts kilometers to miles.
# Formula: 1 kilometer = 0.621371 miles

def km_to_miles(km):
    if km < 0:
        return "Distance cannot be negative"
    return km * 0.621371

# Basic Example
if __name__ == "__main__":
    km1 = 5
    miles1 = km_to_miles(km1)
    print(f"{km1} kilometers is equal to {miles1:.4f} miles")

    # Another example
    km2 = 12.5
    print(f"{km2} kilometers is equal to {km_to_miles(km2):.4f} miles")
