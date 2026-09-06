class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        current=[]
        result=[]
        def verify(row,col):
            if not current:
                return True
            for i,j in current:
                if i-row==0 or j-col==0:
                    return False
                if abs(i-row)==abs(j-col):
                    return False
            return True
        def translate(mylist):
            temp=["".join(["." for _ in range(n)])]*n
            for i,j in mylist:
                temp[i]=temp[i][:j]+"Q"+temp[i][j+1:]
            return temp

        def backtrack(row):
            if row>=n:
                result.append(translate(current.copy()))
                return
            
            
            for j in range(n):
                if verify(row,j):
                    current.append((row,j))
                    backtrack(row+1)
                    current.pop()
        backtrack(0)
        return result



                