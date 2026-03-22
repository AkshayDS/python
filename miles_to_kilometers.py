# Problem: Miles to Kilometers Converter
# Description: Write a function `miles_to_km(miles)` that converts miles to kilometers.
# Formula: 1 mile is approximately 1.60934 kilometers.

def miles_to_km(miles):
    return miles * 1.60934

# Basic Example
if __name__ == "__main__":
    miles = 5
    kilometers = miles_to_km(miles)
    print(f"{miles} miles is equal to {kilometers} kilometers")

    # Another example
    miles2 = 10
    print(f"{miles2} miles is equal to {miles_to_km(miles2)} kilometers")
