{
    "code": "def linear_time_17(string):\n    stack = []\n    for char in string:\n        if char == '(' or char == '[' or char == '{':\n            stack.append(char)\n        elif char == ')' and stack and stack[-1] == '(':\n            stack.pop()\n        elif char == ']' and stack and stack[-1] == '[':\n            stack.pop()\n        elif char == '}' and stack and stack[-1] == '{':\n            stack.pop()\n        else:\n            return False\n    return len(stack) == 0",
    "complexity": "O(n)"
}