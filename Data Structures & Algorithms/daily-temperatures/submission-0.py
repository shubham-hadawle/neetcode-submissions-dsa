class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []     # store pair values: [temperature, index]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:    # Compare temp with the temperature-value of the stack[-1]
                stackTemp, stackInd = stack.pop()
                output[stackInd] = i-stackInd
            stack.append([temp, i])

        return output
