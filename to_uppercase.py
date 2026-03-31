# Problem: Convert String to Uppercase
# Description: Write a function `to_uppercase(text)` that converts a string to uppercase without using built-in upper().

def to_uppercase(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

# Basic Example
if __name__ == "__main__":
    text1 = "hello world"
    result1 = to_uppercase(text1)
    print(f"'{text1}' in uppercase is: '{result1}'")

    # Another example
    text2 = "Python 3"
    print(f"'{text2}' in uppercase is: '{to_uppercase(text2)}'")
