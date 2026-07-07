class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i,j in enumerate(nums):
            if i>0 and j==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                threesum=nums[left]+nums[right]+j
                if threesum>0:
                    right-=1
                elif threesum<0:
                    left+=1
                else:
                    res.append([nums[left],nums[right],j])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
        return res