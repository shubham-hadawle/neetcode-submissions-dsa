class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        
        def dfs(i, j, idx):
            if idx >= len(word) or (i < 0) or (i >= len(board)) or (j < 0) or (j >= len(board[0])) or board[i][j] != word[idx] or (i, j) in visited:
                return False
            
            if idx == len(word)-1:
                return True

            visited.add((i, j))

            result = (dfs(i, j+1, idx+1) or
                dfs(i, j-1, idx+1) or
                dfs(i-1, j, idx+1) or
                dfs(i+1, j, idx+1))

            visited.remove((i, j))

            return result

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                result = dfs(i, j, 0)

                if result:
                    return True

        return False