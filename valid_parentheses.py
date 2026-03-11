"""
Script to validate if a string of brackets is properly formatted.
Demonstrates the classic use case for the 'Stack' data structure (LIFO - Last In First Out).
"""

def is_valid_parentheses(s: str) -> bool:
    """
    Checks if a string containing '(', ')', '{', '}', '[' and ']' is valid.
    A string is valid if open brackets are closed by the same type of brackets 
    and in the correct order.
    """
    # A dictionary to map closing brackets to their corresponding opening brackets
    bracket_map = {")": "(", "}": "{", "]": "["}
    
    # A list functioning as a stack to keep track of opening brackets
    stack = []
    
    for char in s:
        if char in bracket_map:
            # If the character is a closing bracket, pop the top element from the stack
            # If the stack is empty, use a dummy value like '#'
            top_element = stack.pop() if stack else '#'
            
            # If the popped element doesn't match the corresponding opening bracket, return False
            if bracket_map[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
            
    # The string is valid only if the stack is completely empty at the end
    return len(stack) == 0
