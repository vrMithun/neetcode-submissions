class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr=[]
        result=[]
        def backtrack(n):
            if n>=len(nums):
                result.append(curr.copy())
                return
            curr.append(nums[n])
            backtrack(n+1)
            curr.pop()
            backtrack(n+1)
        backtrack(0)
        return result
