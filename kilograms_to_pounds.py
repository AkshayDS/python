# Problem: Kilograms to Pounds Converter
# Description: Write a function `kg_to_lbs(kg)` that converts kilograms to pounds.
# Formula: 1 kilogram is approximately 2.20462 pounds.

def kg_to_lbs(kg):
    return kg * 2.20462

# Basic Example
if __name__ == "__main__":
    weight_kg = 50
    weight_lbs = kg_to_lbs(weight_kg)
    print(f"{weight_kg} kilograms is equal to {weight_lbs} pounds")

    # Another example
    weight2_kg = 10
    print(f"{weight2_kg} kilograms is equal to {kg_to_lbs(weight2_kg)} pounds")
