class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        number_of_islands = 0

        def bfs(r, c):
            dq = collections.deque()
            dq.append((r, c))
            visited.add((r, c))

            while dq:
                r, c = dq.popleft()

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        dq.append((nr, nc))
                        visited.add((nr, nc))

            return

        for r in range(0, rows):
            for c in range(0, cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    number_of_islands += 1
                    bfs(r, c)

        return number_of_islands