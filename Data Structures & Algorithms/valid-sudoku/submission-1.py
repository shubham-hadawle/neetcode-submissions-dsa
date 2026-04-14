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


        # # Checking Rows
        # for i in range(0, 9):
        #     rowSet = set()
        #     for j in range(0, 9):
        #         item = board[i][j]
        #         if item in rowSet:
        #             return False
        #         elif item != '.':
        #             rowSet.add(item)

        # # Checking Columns
        # for i in range(0, 9):
        #     columnSet = set()
        #     for j in range(0, 9):
        #         item = board[i][j]
        #         if item in columnSet:
        #             return False
        #         elif item != '.':
        #             columnSet.add(item)

        # # Checking Grid
        # startingIndex = [
        #     (0, 0), (0, 3), (0, 6),
        #     (3, 0), (3, 3), (3, 6),
        #     (6, 0), (6, 3), (6, 6)
        # ]       # These are the starting indices of all 3x3 grids

        # for start in startingIndex:
        #     r, c = start
        #     gridSet = set()
        #     for i in range(r, r+3):
        #         for j in range(c, c+3):
        #             item = board[i][j]
        #             if item in gridSet:
        #                 return False
        #             elif item != '.':
        #                 gridSet.add(item)

        # return True