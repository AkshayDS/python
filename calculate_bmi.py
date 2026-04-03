# Problem: Calculate Body Mass Index (BMI)
# Description: Write a function `calculate_bmi(weight, height)` that returns the BMI.
# Formula: BMI = weight / (height * height), where weight is in kg and height is in meters.

def calculate_bmi(weight, height):
    return weight / (height * height)

# Basic Example
if __name__ == "__main__":
    weight_kg = 70
    height_m = 1.75
    bmi = calculate_bmi(weight_kg, height_m)
    print(f"For a weight of {weight_kg}kg and height of {height_m}m, the BMI is: {bmi:.2f}")

    # Another example
    w2 = 85
    h2 = 1.80
    print(f"Weight: {w2}kg, Height: {h2}m -> BMI: {calculate_bmi(w2, h2):.2f}")
