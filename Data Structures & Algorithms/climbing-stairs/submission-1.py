class Solution:
    def climbStairs(self, n: int) -> int:
        # DP - Iterative Bottom-Up
        if n <= 2:
            return n

        dp = [0] * (n+1)
        dp[0], dp[1], dp[2] = 0, 1, 2

        for i in range(3, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

        # # DP - Recursive Top-Down
        # dp = [-1] * (n)

        # def dfs(i):
        #     if i == n:
        #         return 1
        #     elif i > n:
        #         return 0
        #     else:
        #         if dp[i] == -1:
        #             dp[i] = dfs(i + 1) + dfs(i + 2)

        #         return dp[i]
        
        # return dfs(0)