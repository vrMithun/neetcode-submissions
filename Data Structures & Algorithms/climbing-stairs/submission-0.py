class Solution:
    def climbStairs(self, n: int) -> int:
        mylist=[-1]*(n+1)
        def backtrack(t):

            if t==1:
                mylist[1]=1
                return mylist[1]
            if t==2:
                mylist[2]=2
                return mylist[2]
            if mylist[t]!=-1:
                return mylist[t]
            mylist[t]=backtrack(t-1)+backtrack(t-2)
            return mylist[t]
        return backtrack(n)
        