class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS + Changing '1' to '0' after visiting
        numOfIslands = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0) or (r >= ROWS) or (c < 0) or (c >= COLS) or grid[r][c] == "0":
                return

            else:
                grid[r][c] = "0"
                dfs(r - 1, c)
                dfs(r, c - 1)
                dfs(r + 1, c)
                dfs(r, c + 1)

        for r in range(0, ROWS):
            for c in range(0, COLS):
                if grid[r][c] == "1":
                    numOfIslands += 1
                    dfs(r, c)

        return numOfIslands