class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        current=[]
        result=[[]]
        nums.sort()
        mydict=dict()
        def backtrack(index):
            if index>=len(nums):
                if tuple(current) not in mydict:
                    result.append(current.copy())
                return
            
            for i in range(index,len(nums)):
                if i>index and nums[i]==nums[index]:
                    continue
                current.append(nums[i])
                if tuple(current) not in mydict:
                    mydict[tuple(current.copy())]=1
                    result.append(current.copy())
                backtrack(i+1)
                current.pop()
        backtrack(0)
        return result