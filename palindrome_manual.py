"""
Script to check if a string is a palindrome without using built-in string/list functions 
like `::-1`, `reverse()`, `.lower()`, or `.isalnum()`.
"""

def is_palindrome_manual(s: str) -> bool:
    """
    Checks if a string is a palindrome manually using two pointers
    and ASCII value checking.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # 1. Skip non-alphanumeric from the left manually
        char_left = s[left]
        # Check if ASCII is between a-z, A-Z, or 0-9
        is_alnum_left = ('a' <= char_left <= 'z') or ('A' <= char_left <= 'Z') or ('0' <= char_left <= '9')
        if not is_alnum_left:
            left += 1
            continue
            
        # 2. Skip non-alphanumeric from the right manually
        char_right = s[right]
        is_alnum_right = ('a' <= char_right <= 'z') or ('A' <= char_right <= 'Z') or ('0' <= char_right <= '9')
        if not is_alnum_right:
            right -= 1
            continue
            
        # 3. Manual lowercase conversion for comparison
        # If uppercase (A-Z is 65-90), convert to lowercase (a-z is 97-122) by adding 32
        if 'A' <= char_left <= 'Z':
            char_left = chr(ord(char_left) + 32)
            
        if 'A' <= char_right <= 'Z':
            char_right = chr(ord(char_right) + 32)

        # 4. Compare the characters
        if char_left != char_right:
            return False
            
        # Move pointers inward
        left += 1
        right -= 1
        
    return True

# --- Test Executions ---
if __name__ == "__main__":
    test_cases = [
        "racecar",
        "A man, a plan, a canal: Panama",
        "hello",
        "No 'x' in Nixon",
        "12321",
        "123a321"
    ]
    
    print("--- Palindrome Check (No Built-ins) ---")
    for phrase in test_cases:
        result = is_palindrome_manual(phrase)
        status = "✅ True" if result else "❌ False"
        print(f"'{phrase}':\n  -> {status}\n")
