class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        right=len(matrix)-1
        
        while left<=right:
            mid=(right-left)//2+left
            if target==matrix[mid][0]:
                return True
            elif self.tocontinue(matrix[mid],target):
                return self.binarysearch(target,matrix[mid])
            elif target>matrix[mid][0]:
                left=mid+1
            else:
                right=mid-1
        return False
                
    def tocontinue(self,mylist,target):
        return mylist[0] <= target <= mylist[-1]
    def binarysearch(self,target,mylist):
        left=0
        right=len(mylist)-1
        
        while left<=right:
            mid=(right-left)//2+left
            if mylist[mid]==target:
                return True
            elif mylist[mid]>target:
                right=mid-1
            else:
                left=mid+1
                
        return False