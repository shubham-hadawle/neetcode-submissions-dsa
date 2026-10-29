class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(0, n)]

        cols = set()
        negDia = set()
        posDia = set()

        result = []
        soln = []

        def dfs(r):
            if r == n:
                soln = ["".join(row) for row in board]
                result.append(soln.copy())
                return result

            for c in range(0, n):
                if c in cols or (r-c) in negDia or (r+c) in posDia:
                    continue
                
                cols.add(c)
                negDia.add(r-c)
                posDia.add(r+c)
                board[r][c] = "Q"

                dfs(r+1)

                cols.remove(c)
                negDia.remove(r-c)
                posDia.remove(r+c)
                board[r][c] = "."

            return

        dfs(0)
        return result