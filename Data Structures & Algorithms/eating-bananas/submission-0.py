class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        while left<=right:
            mid=(right-left)//2+left
            currtime=self.helper(mid,piles)
            if h>=currtime:
                right=mid-1
            else:
                left=mid+1
        return left
        
    def helper(self,rate,mylist):
        result=0
        for i in mylist:
            time=i//rate
            if i%rate==0:
                result+=time
            else:
                result+=time+1
        return result