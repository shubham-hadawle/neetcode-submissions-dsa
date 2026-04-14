class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if s == "":
            return True

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif char == ')' or char == ']' or char == '}':
                if not stack:   # If the stack is empty
                    return False
                c = stack.pop()
                if c == '(' and char == ')':
                    continue
                elif c == '[' and char == ']':
                    continue
                elif c == '{' and char == '}':
                    continue
                else:
                    return False
            else:
                return False
        
        if not stack:
            return True
        else:
            return False