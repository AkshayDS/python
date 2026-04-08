# Problem: Generate a Random Number
# Description: Write a function `generate_random(start, end)` that returns a random integer between start and end (inclusive).

import random

def generate_random(start, end):
    return random.randint(start, end)

# Basic Example
if __name__ == "__main__":
    start_val = 1
    end_val = 100
    random_num = generate_random(start_val, end_val)
    print(f"Random number between {start_val} and {end_val}: {random_num}")

    # Another example
    start2 = 50
    end2 = 60
    print(f"Random number between {start2} and {end2}: {generate_random(start2, end2)}")
