class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()     # (r+c) is common
        negaDiag = set()    # (r-c) is common

        result = []
        board = [["."]*n for i in range(0, n)]

        def dfs(r):
            if r == n:
                soln = ["".join(row) for row in board]
                result.append(soln)
                return

            for c in range(0, n):
                if c in col or (r+c) in posDiag or (r-c) in negaDiag:
                    continue

                col.add(c)
                posDiag.add(r+c)
                negaDiag.add(r-c)
                board[r][c] = "Q"

                dfs(r + 1)

                col.remove(c)
                posDiag.remove(r+c)
                negaDiag.remove(r-c)
                board[r][c] = "."

        dfs(0)
        return result