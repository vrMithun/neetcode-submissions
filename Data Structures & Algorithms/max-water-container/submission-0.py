class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        result=0
        while left<right:
            temp=min(heights[right],heights[left])*(right-left)
            result=max(result,temp)
            if heights[left]>=heights[right]:
                right-=1
            else:
                left+=1
        return result
