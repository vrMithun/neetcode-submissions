class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        left=0
        right=0
        mydict=dict()
        for i in range(len(s1)):
            if s1[i] not in mydict:
                mydict[s1[i]]=1
            else:
                mydict[s1[i]]+=1
        tempdict=mydict.copy()
        while right<len(s2):
            
            if s2[right] in tempdict and tempdict[s2[right]]>0:
                tempdict[s2[right]]-=1
                if sum(tempdict.values())==0:
                    return True
                right+=1
            else:
                tempdict=mydict.copy()
                left+=1
                right=left
        return False





