class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        hashRow = collections.defaultdict(set)
        hashCol = collections.defaultdict(set)
        hashGrid = collections.defaultdict(set)

        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    continue
                if (board[i][j] in hashRow[i] or 
                    board[i][j] in hashCol[j] or 
                    board[i][j] in hashGrid[i//3, j//3]):
                    return False
                
                hashRow[i].add(board[i][j])
                hashCol[j].add(board[i][j])
                hashGrid[(i//3, j//3)].add(board[i][j])
        return True
