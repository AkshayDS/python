# Problem: Percentage Calculator
# Description: Write a function `calculate_percentage(obtained, total)` that returns the percentage.
# Formula: Percentage = (obtained / total) * 100

def calculate_percentage(obtained, total):
    return (obtained / total) * 100

# Basic Example
if __name__ == "__main__":
    obtained = 45
    total = 60
    percentage = calculate_percentage(obtained, total)
    print(f"Obtained: {obtained}/{total} -> Percentage: {percentage}%")

    # Another example
    print(f"Obtained: 80/100 -> Percentage: {calculate_percentage(80, 100)}%")
