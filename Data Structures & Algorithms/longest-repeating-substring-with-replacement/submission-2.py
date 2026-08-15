class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s==" ":
            return 1
        left=0
        right=0
        mydict=dict()
        result=0
        while right<len(s):
            if s[right] not in mydict:
                mydict[s[right]]=1
            else:
                mydict[s[right]]+=1
            currmax=max(mydict.values())
            tempk=right-left+1-currmax
            if tempk<=k:
                result=max(result,right-left+1)
                right+=1
            else:
                while tempk>k:
                    mydict[s[left]]-=1
                    left+=1
                    currmax=max(mydict.values())
                    tempk=right-left+1-currmax
                right+=1
        return result
                
            
            