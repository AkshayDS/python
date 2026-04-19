# Problem: Convert Grams to Kilograms
# Description: Write a function `grams_to_kg(grams)` that converts grams to kilograms.
# Formula: 1 kilogram = 1000 grams

def grams_to_kg(grams):
    if grams < 0:
        return "Weight cannot be negative"
    return grams / 1000

# Basic Example
if __name__ == "__main__":
    g1 = 500
    kg1 = grams_to_kg(g1)
    print(f"{g1} grams is equal to {kg1} kilograms")

    # Another example
    g2 = 2500
    print(f"{g2} grams is equal to {grams_to_kg(g2)} kilograms")
