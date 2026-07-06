class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset=set(nums)
        result=0
        for i in nums:
            if i-1 not in myset:
                next_num=i+1
                length=1
                while next_num in myset:
                    length+=1
                    next_num+=1
                result=max(result,length)
        return result