# Problem: Convert Hours to Seconds
# Description: Write a function `hours_to_seconds(hours)` that converts hours to seconds.
# Formula: 1 hour = 3600 seconds.

def hours_to_seconds(hours):
    return hours * 3600

# Basic Example
if __name__ == "__main__":
    h1 = 2
    seconds1 = hours_to_seconds(h1)
    print(f"{h1} hours is equal to {seconds1} seconds")

    # Another example
    h2 = 5.5
    print(f"{h2} hours is equal to {hours_to_seconds(h2)} seconds")
