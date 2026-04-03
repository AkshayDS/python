# Problem: Concatenate Two Strings
# Description: Write a function `concatenate(str1, str2)` that joins two strings together with a space in between.

def concatenate(str1, str2):
    return str1 + " " + str2

# Basic Example
if __name__ == "__main__":
    first_name = "John"
    last_name = "Doe"
    full_name = concatenate(first_name, last_name)
    print(f"First Name: '{first_name}', Last Name: '{last_name}' -> Full Name: '{full_name}'")

    # Another example
    word1 = "Hello"
    word2 = "World"
    print(f"'{word1}' and '{word2}' concatenated: '{concatenate(word1, word2)}'")
