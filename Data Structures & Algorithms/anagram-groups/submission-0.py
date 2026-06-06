class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        selected=[0 for i in range(len(strs))]
        mydict={}
        def isanagram(s,t)->bool:
            if len(s)!=len(t):
                return False
            countS,countT={},{}
            for i in range(len(s)):
                countS[s[i]] = 1 + countS.get(s[i], 0)
                countT[t[i]] = 1 + countT.get(t[i], 0)
            return countS == countT
        for i in range(len(strs)):
            if selected[i]:
                continue
            selected[i]=1
            mydict[strs[i]]=[strs[i]]
            for j in range(i+1,len(strs)):
                if selected[j]:
                    continue
                elif isanagram(strs[i],strs[j]):
                    mydict[strs[i]].append(strs[j])
                    selected[j]=1
        return list(mydict.values())
