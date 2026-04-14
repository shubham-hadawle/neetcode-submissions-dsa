class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0

        ROWS, COLS = len(grid), len(grid[0])
        # visited = set()
        dq = deque()

        def multi_source_bfs(r, c, fresh):
            # Check if a 'Fresh Orange' exists at this place
            if (r < 0) or (r >= ROWS) or (c < 0) or (c >= COLS) or (grid[r][c] != 1):
                return fresh
            else:
                grid[r][c] = 2
                fresh -= 1
                dq.append((r, c))
                return fresh


        for r in range(0, ROWS):
            for c in range(0, COLS):
                # Count the number of Fresh Oranges
                if grid[r][c] == 1:
                    fresh += 1
                # Append the Rotten Oranges to the Deque
                if grid[r][c] == 2:
                    dq.append((r, c))


        while (fresh > 0) and (dq):
            for i in range(0, len(dq)):
                r, c = dq.popleft()
                fresh = multi_source_bfs(r + 1, c, fresh)
                fresh = multi_source_bfs(r, c + 1, fresh)
                fresh = multi_source_bfs(r - 1, c, fresh)
                fresh = multi_source_bfs(r, c - 1, fresh)
            time += 1

        if fresh == 0:
            return time
        else:
            return -1