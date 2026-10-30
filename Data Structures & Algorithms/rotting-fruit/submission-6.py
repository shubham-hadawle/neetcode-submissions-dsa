class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        dq = collections.deque()

        def bfs(r, c, number_of_fresh):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in visited:
                return number_of_fresh

            number_of_fresh -= 1
            grid[r][c] = 2
            dq.append((r, c))
            visited.add((r, c))

            return number_of_fresh

        number_of_fresh = 0

        for r in range(0, rows):
            for c in range(0, cols):
                if grid[r][c] == 1:
                    number_of_fresh += 1

                if grid[r][c] == 2:
                    dq.append((r, c))
                    visited.add((r, c))

        time = 0

        while dq and number_of_fresh > 0:
            for i in range(0, len(dq)):
                r, c = dq.popleft()

                # grid[r][c] = time

                number_of_fresh = bfs(r+1, c, number_of_fresh)
                number_of_fresh = bfs(r-1, c, number_of_fresh)
                number_of_fresh = bfs(r, c+1, number_of_fresh)
                number_of_fresh = bfs(r, c-1, number_of_fresh)

            time += 1

        if number_of_fresh <= 0:
            return time
        else:
            return -1