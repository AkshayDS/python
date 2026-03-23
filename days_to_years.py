# Problem: Days to Years Converter
# Description: Write a function `days_to_years(days)` that converts a given number of days into years, weeks, and days.
# Assume 1 year = 365 days and 1 week = 7 days for simplicity.

def days_to_years(days):
    years = days // 365
    remaining_days = days % 365
    weeks = remaining_days // 7
    final_days = remaining_days % 7
    return years, weeks, final_days

# Basic Example
if __name__ == "__main__":
    total_days = 400
    y, w, d = days_to_years(total_days)
    print(f"{total_days} days is equal to {y} years, {w} weeks, and {d} days")

    # Another example
    total_days2 = 1000
    y2, w2, d2 = days_to_years(total_days2)
    print(f"{total_days2} days is equal to {y2} years, {w2} weeks, and {d2} days")
