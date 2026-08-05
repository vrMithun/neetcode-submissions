class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mylist=[]
        result=0
        for i in range(len(position)):
            yet_to_cover=target-position[i]
            time=yet_to_cover/speed[i]
            mylist.append((yet_to_cover,time))

        mylist=sorted(mylist,key=lambda x:x[0])
        templist=[]
        for dist,time in mylist:
            if not templist or templist[-1][1]<time:
                result+=1
            else:
                time=templist[-1][1]
            templist.append((dist,time))
        return result
            