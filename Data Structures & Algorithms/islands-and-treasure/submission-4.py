class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        dq = collections.deque()

        def bfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == -1 or (r, c) in visited:
                return

            dq.append((r, c))
            visited.add((r, c))
            return

        for r in range(0, rows):
            for c in range(0, cols):
                if grid[r][c] == 0:
                    dq.append((r, c))
                    visited.add((r, c))

        dist = 0

        while dq:
            for i in range(0, len(dq)):
                r, c = dq.popleft()

                grid[r][c] = dist

                bfs(r+1, c)
                bfs(r-1, c)
                bfs(r, c+1)
                bfs(r, c-1)

            dist += 1

        return