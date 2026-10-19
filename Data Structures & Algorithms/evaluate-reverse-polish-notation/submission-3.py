class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for char in tokens:
            if char in operators:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if char == "+":
                    stack.append(num1 + num2)
                elif char == "-":
                    stack.append(num1 - num2)
                elif char == "*":
                    stack.append(num1 * num2)
                elif char == "/":
                    stack.append(int(float(num1)/num2))

            else:
                stack.append(char)

        return int(stack.pop())