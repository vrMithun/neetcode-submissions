class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydict=dict()
        for i in s:
            if i not in mydict:
                mydict[i]=1
            else:
                mydict[i]+=1
        for j in t:
            if j not in mydict or mydict[j]==0:
                return False
            else:
                mydict[j]-=1
        for k in mydict.values():
            if k>0:
                return False
        return True
            
        