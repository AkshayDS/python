# Problem: Convert Days to Hours
# Description: Write a function `days_to_hours(days)` that converts days to hours.
# Formula: 1 day = 24 hours

def days_to_hours(days):
    if days < 0:
        return "Days cannot be negative"
    return days * 24

# Basic Example
if __name__ == "__main__":
    d1 = 5
    hours1 = days_to_hours(d1)
    print(f"{d1} days is equal to {hours1} hours")

    # Another example
    d2 = 2.5
    print(f"{d2} days is equal to {days_to_hours(d2)} hours")
