# Problem: Swap Two Variables
# Description: Write a function `swap(a, b)` that returns the values swapped.

def swap(a, b):
    # In Python, swapping can be done easily with tuple unpacking
    # temp = a
    # a = b
    # b = temp
    # return a, b
    return b, a

# Basic Example
if __name__ == "__main__":
    x = 10
    y = 20
    print(f"Before swap: x = {x}, y = {y}")
    
    x, y = swap(x, y)
    print(f"After swap: x = {x}, y = {y}")

    # Another example
    var1 = "Hello"
    var2 = "World"
    print(f"\nBefore swap: var1 = '{var1}', var2 = '{var2}'")
    var1, var2 = swap(var1, var2)
    print(f"After swap: var1 = '{var1}', var2 = '{var2}'")
