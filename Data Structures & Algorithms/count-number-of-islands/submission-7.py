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


        # # BFS (Iterative with Deque)
        # if not grid:
        #     return 0

        # numOfIslands = 0
        # ROWS, COLS = len(grid), len(grid[0])
        # visited = set()

        # def bfs(r, c):
        #     dq = collections.deque()
        #     visited.add((r, c))
        #     dq.append((r, c))

        #     while dq:
        #         r, c = dq.popleft()     # Converting 'dq.popleft()' to 'dq.pop()' makes this code an Iterative DFS with Stack
        #         directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        #         for dr, dc in directions:
        #             row, col = (r + dr), (c + dc)
        #             if (row in range(0, ROWS) and col in range(0, COLS) 
        #                 and grid[row][col] == '1' and (row, col) not in visited):
        #                 dq.append((row, col))
        #                 visited.add((row, col))

        # for r in range(0, ROWS):
        #     for c in range(0, COLS):
        #         if grid[r][c] == '1' and (r, c) not in visited:
        #             bfs(r, c)
        #             numOfIslands += 1

        # return numOfIslands

