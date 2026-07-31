class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mystack=[]
        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                mystack.append(i)
            else:
                val1=int(mystack.pop())
                val2=int(mystack.pop())
                if i=="+":
                    mystack.append(val2+val1)
                elif i=="-":
                    mystack.append(val2-val1)
                elif i=="/":
                    mystack.append(int(val2/val1))
                elif i=="*":
                    mystack.append(val1*val2)
        return int(mystack.pop())