class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mystack=[]
        result=[0]*len(temperatures)
        for index,val in enumerate(temperatures):
            if not mystack:
                mystack.append((index,val))
            while mystack and mystack[-1][1]<val:
                tempindex,tempval=mystack.pop()
                result[tempindex]=index-tempindex
            mystack.append((index,val))
        for ndex,_ in mystack:
            result[index]=0
        return result