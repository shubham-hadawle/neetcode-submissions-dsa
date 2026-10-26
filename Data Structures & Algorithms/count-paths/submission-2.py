class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Right Way to Form an Empty DP Table
        dp = [[0] * n for i in range(0, m)]

        for i in range(0, n):
            dp[m-1][i] = 1

        for i in range(0, m):
            dp[i][n-1] = 1

        # When filling a 2D DP Table in the Bottom-Up Approach, always traverse in Reverse Order
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]

        return dp[0][0]