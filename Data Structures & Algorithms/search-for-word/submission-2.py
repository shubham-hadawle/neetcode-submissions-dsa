class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(r, c, i):
            if i == len(word):
                # End of word length reached - Word Found
                return True

            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visit or
                word[i] != board[r][c]):
                return False

            # If all the above conditions are not met then,
            # the correct character for the correct word index has been Found.
            visit.add((r, c))
            result = (dfs(r + 1, c, i + 1) or
                      dfs(r - 1, c, i + 1) or
                      dfs(r, c + 1, i + 1) or
                      dfs(r, c - 1, i + 1))
            # Returned from the DFS depth call for the entire word, hence now remove (r, c) from visited characters.
            visit.remove((r, c))
            return result

        for r in range(0, ROWS):
            for c in range(0, COLS):
                output = dfs(r, c, 0)
                if output == True:
                    return True

        return False
