# Problem: Average of Numbers
# Description: Write a function `calculate_average(numbers)` that returns the average of a list of numbers.

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Basic Example
if __name__ == "__main__":
    nums = [10, 20, 30, 40, 50]
    avg = calculate_average(nums)
    print(f"The average of {nums} is: {avg}")

    # Another example
    nums2 = [5, 15, 25]
    print(f"Average of {nums2} is: {calculate_average(nums2)}")
