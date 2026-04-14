class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        # currArea = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, currArea):
            if (r < 0) or (r >= ROWS) or (c < 0) or (c >= COLS) or \
                (grid[r][c] == 0):
                return currArea
            else:
                grid[r][c] = 0
                currArea += 1

                # if currArea > maxArea:
                #     maxArea = currArea

                # Recursive calls in all 4 directions
                currArea = dfs(r - 1, c, currArea)
                currArea = dfs(r, c + 1, currArea)
                currArea = dfs(r + 1, c, currArea)
                currArea = dfs(r, c - 1, currArea)
                return currArea

        for r in range(0, ROWS):
            for c in range(0, COLS):
                if grid[r][c] == 1:
                    currArea = 0
                    currArea = dfs(r, c, currArea)
                    maxArea = max(currArea, maxArea)

        return maxArea