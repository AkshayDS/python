# Problem: Convert List to String
# Description: Write a function `list_to_string(lst, separator)` that converts a list of strings into a single string, joined by the given separator.

def list_to_string(lst, separator=" "):
    return separator.join(lst)

# Basic Example
if __name__ == "__main__":
    words = ["Python", "is", "awesome"]
    print(f"List: {words}")
    print(f"String with space separator: '{list_to_string(words)}'")

    items = ["apple", "banana", "cherry"]
    print(f"\nList: {items}")
    print(f"String with comma separator: '{list_to_string(items, ', ')}'")
