class Solution:
    def isValid(self, s: str) -> bool:
        mydict={"(":")","[":"]","{":"}"}
        if len(s)%2!=0:
            return False
        mystack=[]
        for i in s:
            if not mystack and i not in mydict:
                return False
            if i in mydict:
                mystack.append(i)
            elif i not in mydict and mydict[mystack[-1]]==i:
                mystack.pop(-1)
            else:
                return False
        if mystack:
            return False
        return True
            