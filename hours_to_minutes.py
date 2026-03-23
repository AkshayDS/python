# Problem: Hours to Minutes Converter
# Description: Write a function `hours_to_minutes(hours)` that converts hours to minutes.
# Formula: 1 hour = 60 minutes.

def hours_to_minutes(hours):
    return hours * 60

# Basic Example
if __name__ == "__main__":
    hours1 = 2.5
    minutes1 = hours_to_minutes(hours1)
    print(f"{hours1} hours is equal to {minutes1} minutes")

    # Another example
    hours2 = 5
    print(f"{hours2} hours is equal to {hours_to_minutes(hours2)} minutes")
