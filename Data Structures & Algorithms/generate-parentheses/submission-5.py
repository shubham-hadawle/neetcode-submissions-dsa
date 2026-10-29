class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        soln = []

        def dfs(open, close):
            nonlocal result, soln

            if open == n and close == n:
                result.append("".join(soln))
                return

            if open < n:
                soln.append("(")
                dfs(open+1, close)
                soln.pop()

            if close < open:
                soln.append(")")
                dfs(open, close+1)
                soln.pop()

            return

        dfs(0, 0)
        return result