class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right=len(nums)-1
        left=0
        
        while left<=right:
            currindex=(right-left)//2+left
            if target==nums[currindex]:
                return currindex
            elif target<nums[currindex]:
                right=currindex-1
            else:
                left=currindex+1
                
        return -1
                