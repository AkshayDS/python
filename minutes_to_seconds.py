# Problem: Minutes to Seconds Converter
# Description: Write a function `minutes_to_seconds(minutes)` that converts minutes to seconds.
# Formula: 1 minute = 60 seconds.

def minutes_to_seconds(minutes):
    return minutes * 60

# Basic Example
if __name__ == "__main__":
    minutes1 = 5
    seconds1 = minutes_to_seconds(minutes1)
    print(f"{minutes1} minutes is equal to {seconds1} seconds")

    # Another example
    minutes2 = 1.5
    print(f"{minutes2} minutes is equal to {minutes_to_seconds(minutes2)} seconds")
