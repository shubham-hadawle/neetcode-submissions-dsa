class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        number_of_islands = 0

        def dfs(r, c, island_continued):
            nonlocal number_of_islands

            if (r < 0) or (c < 0) or (r >= rows) or (c >= cols) or ((r, c) in visited) or (grid[r][c] == "0"):
                return

            if not island_continued:
                number_of_islands += 1
            visited.add((r, c))

            dfs(r+1, c, True)
            dfs(r-1, c, True)
            dfs(r, c+1, True)
            dfs(r, c-1, True)

            return
        
        for r in range(0, rows):
            for c in range(0, cols):
                dfs(r, c, False)

        return number_of_islands