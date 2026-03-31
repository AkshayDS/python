# Problem: Count Characters in a String
# Description: Write a function `count_char(text, char)` that counts how many times a character appears in a string.

def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

# Basic Example
if __name__ == "__main__":
    text = "hello world"
    char = "l"
    result = count_char(text, char)
    print(f"The character '{char}' appears {result} times in '{text}'")

    # Another example
    print(f"'o' appears {count_char('programming', 'g')} times in 'programming'")
