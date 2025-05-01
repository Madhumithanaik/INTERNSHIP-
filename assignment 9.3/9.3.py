def is_balanced(s):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in matching.values():
            stack.append(char)
        elif char in matching.keys():
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
    
    return not stack

input_string = "([{}])"
print(is_balanced(input_string))
