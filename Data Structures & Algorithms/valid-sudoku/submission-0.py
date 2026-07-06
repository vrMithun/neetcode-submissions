class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # checking rows
        for i in range(0,9):
            myset=set()
            for j in range(0,9):
                if board[i][j] in myset:
                    return False
                elif board[i][j]!=".":
                    myset.add(board[i][j])

        # checking column
        for i in range(0,9):
            myset=set()
            for j in range(0,9):
                if board[j][i] in myset:
                    return False
                elif board[j][i]!=".":
                    myset.add(board[j][i])

        # checking box
        starts=[(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        for i,j in starts:
            myset=set()
            for row in range(i,i+3):
                for col in range(j,j+3):
                    if board[row][col] in myset:
                        return False
                    if board[row][col]!=".":
                        myset.add(board[row][col])
        return True


