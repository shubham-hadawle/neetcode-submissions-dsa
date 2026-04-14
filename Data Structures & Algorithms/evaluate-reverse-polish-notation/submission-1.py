class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tk in tokens:
            if stack and tk == '+':
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(val1+val2)

            elif tk == '-':
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(val1-val2)

            elif tk == '*':
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(val1*val2)

            elif tk == '/':
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(val1/val2)

            else:
                stack.append(tk)

        if len(stack) == 1:
            return int(stack.pop())