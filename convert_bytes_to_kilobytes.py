# Problem: Convert Bytes to Kilobytes
# Description: Write a function `bytes_to_kb(bytes)` that converts bytes to kilobytes.
# Formula: 1 Kilobyte (KB) = 1024 Bytes

def bytes_to_kb(bytes_val):
    if bytes_val < 0:
        return "Given value cannot be negative"
    return bytes_val / 1024

# Basic Example
if __name__ == "__main__":
    b1 = 2048
    kb1 = bytes_to_kb(b1)
    print(f"{b1} bytes is equal to {kb1} kilobytes")

    # Another example
    b2 = 5000
    print(f"{b2} bytes is equal to {bytes_to_kb(b2):.2f} kilobytes")
