class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP - Bottom-Up Approach
        row = [1] * n

        for i in range(0, m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow

        return row[0]