class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        current=[]
        result=[]
        visited=[False]*len(nums)
        def backtrack():
            if len(current)==len(nums):
                result.append(current.copy())
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                visited[i]=True
                current.append(nums[i])
                backtrack()
                current.pop()
                visited[i]=False
        backtrack()
        return result