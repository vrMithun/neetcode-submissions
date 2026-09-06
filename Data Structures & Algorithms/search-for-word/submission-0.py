class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited=set()
        current=[]
        def backtrack(row,col):
            if row<0 or row>=len(board) or col<0 or col>=len(board[0]):
                return False
            if (row,col) in visited:
                return False
            
            if word[len(current)]!=board[row][col]:
                return False

            current.append(board[row][col])
            visited.add((row,col))
            if len(current)==len(word):
                return True
            
            moves={(1,0),(0,1),(-1,0),(0,-1)}
            for i,j in moves:
                if backtrack(row+i,col+j):
                    return True
            current.pop()
            visited.remove((row, col))

            return False
        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(row, col):
                    return True
        return False
        
            
