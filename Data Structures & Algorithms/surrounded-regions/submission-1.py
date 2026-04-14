class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        store, visited = set(), set()

        # DFS for 'Unsurrounded Os' to 'Temporary Ts'
        def dfs(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or \
                board[r][c] != 'O'):
                return
            else:
                board[r][c] = 'T'
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
                return

        # Convert unsurrounded O -> T
        for r in range(0, ROWS):
            for c in range(0, COLS):
                if (board[r][c] == 'O') and (r in [0, ROWS-1] or c in [0, COLS-1]):
                    dfs(r, c)

        # Convert surrounded O -> X
        for r in range(0, ROWS):
            for c in range(0, COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # Convert T -> O
        for r in range(0, ROWS):
            for c in range(0, COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'

        return