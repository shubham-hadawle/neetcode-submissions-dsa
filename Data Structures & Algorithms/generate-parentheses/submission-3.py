class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result, soln = [], []

        def dfs(openN, closeN):
            if openN == closeN == n:
                # Valid Solution is Found.
                result.append("".join(soln))
                return

            if openN < n:
                soln.append("(")
                dfs(openN + 1, closeN)
                soln.pop()

            if closeN < openN:
                soln.append(")")
                dfs(openN, closeN + 1)
                soln.pop()

        dfs(0, 0)
        return result