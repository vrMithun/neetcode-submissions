class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        current=[]
        result=[]
        def backtrack(index,target):
            if target<0:
                return
            if index>=len(nums):
                return
            if target==0:
                result.append(current.copy())
                return
            current.append(nums[index])
            backtrack(index,target-nums[index])
            current.pop()
            backtrack(index+1,target)
        backtrack(0,target)
        return result

            
        