class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        number_of_islands = 0

        def dfs(r, c):
            nonlocal number_of_islands, visited

            if (r < 0) or (c < 0) or (r >= rows) or (c >= cols) or (r, c) in visited or (grid[r][c] == "0"):
                return

            visited.add((r, c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            return
        
        for r in range(0, rows):
            for c in range(0, cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    number_of_islands += 1
                    dfs(r, c)

        return number_of_islands