class MinStack:

    def __init__(self):
        self.mylist=[]
        self.minval=float("+inf")

    def push(self, val: int) -> None:
        self.minval=min(self.minval,val)
        self.mylist.append((val,self.minval))

    def pop(self) -> None:
        popval=self.mylist.pop()
        if self.mylist:
            self.minval=self.mylist[-1][1]
        else:
            self.minval=float("+inf")
        return popval[0]

    def top(self) -> int:
        return self.mylist[-1][0]

    def getMin(self) -> int:
        return self.minval
        
