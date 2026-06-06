class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict={}
        for i in range(len(nums)):
            mydict[nums[i]]=1+mydict.get(nums[i],0)
        mydict=dict(sorted(mydict.items(),key=lambda x:x[1],reverse=True))
        return list(mydict.keys())[:k]