class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        maxArea = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))

            area = 1 + (dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))
            return area

        for r in range(0, rows):
            for c in range(0, cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    result = dfs(r, c)
                    maxArea = max(maxArea, result)

        return maxArea