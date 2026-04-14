from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Multi-source BFS
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        dq = deque()

        def bfs(r, c):
            if (r < 0) or (r >= ROWS) or (c < 0) or (c >= COLS) or \
                (grid[r][c] == -1) or ((r, c) in visited):
                return
            else:
                visited.add((r, c))
                dq.append((r, c))

        for r in range(0, ROWS):
            for c in range(0, COLS):
                if grid[r][c] == 0 and (r, c) not in visited:
                    dq.append((r, c))
                    visited.add((r, c))

        dist = 0
        while dq:
            for i in range(0, len(dq)):
                r, c = dq.popleft()
                grid[r][c] = dist
                bfs(r + 1, c)
                bfs(r, c + 1)
                bfs(r - 1, c)
                bfs(r, c - 1)
            dist += 1