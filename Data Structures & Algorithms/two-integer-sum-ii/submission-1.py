class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mydict=dict()
        for i in range(len(numbers)):
            if target-numbers[i] in mydict:
                return [mydict[target-numbers[i]]+1,i+1]
            else:
                mydict[numbers[i]]=i
        return
