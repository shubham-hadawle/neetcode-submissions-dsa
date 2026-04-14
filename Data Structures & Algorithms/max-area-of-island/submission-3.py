class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c, currArea):
            if (r < 0) or (r >= ROWS) or (c < 0) or (c >= COLS) or \
                (grid[r][c] == 0 or (r, c) in visited):
                return (currArea + 0)

            else:
                currArea += 1
                visited.add((r, c))
                currArea = dfs(r+1, c, currArea)
                currArea = dfs(r, c+1, currArea)
                currArea = dfs(r-1, c, currArea)
                currArea = dfs(r, c-1, currArea)
                return currArea

        for r in range(0, ROWS):
            for c in range(0, COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    currArea = dfs(r, c, 0)
                    maxArea = max(maxArea, currArea)

        return maxArea
