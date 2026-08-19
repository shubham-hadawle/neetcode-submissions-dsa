class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for char in s:
            if char == '(':
                leftMin += 1
                leftMax += 1

            elif char == ')':
                leftMin -= 1
                leftMax -= 1

            else:       # Considering '*' as any possible character.
                leftMin -= 1
                leftMax += 1

            if leftMax < 0:     # Too many closing parenthsis ')'. Invalid string.
                return False

            if leftMin < 0:
                leftMin = 0     # Reset the range to not be negative. Only consider valid options.

        if leftMin == 0:
            return True
        else:
            return False