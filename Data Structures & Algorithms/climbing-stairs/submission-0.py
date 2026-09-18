class Solution:
    def climbStairs(self, n: int) -> int:
        # DP - Recursive Top-Down
        dp = [-1] * (n)

        def dfs(i):
            if i == n:
                return 1
            elif i > n:
                return 0
            else:
                if dp[i] == -1:
                    dp[i] = dfs(i + 1) + dfs(i + 2)

                return dp[i]
        
        return dfs(0)