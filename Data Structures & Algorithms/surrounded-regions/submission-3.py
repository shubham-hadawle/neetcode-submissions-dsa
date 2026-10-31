class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or board[r][c] != "O":
                return
            
            board[r][c] = "T"
            visited.add((r, c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            return

        for c in range(0, cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows-1][c] == "O":
                dfs(rows-1, c)

        for r in range(0, rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols-1] == "O":
                dfs(r, cols-1)

        for r in range(0, rows):
            for c in range(0, cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                
        for r in range(0, rows):
            for c in range(0, cols):
                if board[r][c] == "T":
                    board[r][c] = "O"