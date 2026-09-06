class Solution:
    def partition(self, s: str) -> List[List[str]]:
        current=[]
        result=[]
        def validate(s,i,j):
            if s[i:j+1][::-1]==s[i:j+1]:
                return True
            return False
            
        def backtrack(index):
            if index>=len(s):
                result.append(current.copy())
                return
            for i in range(index,len(s)):
                if validate(s,index,i):
                    current.append(s[index:i+1])
                    backtrack(i+1)
                    current.pop()

        backtrack(0)
        return result

                
            