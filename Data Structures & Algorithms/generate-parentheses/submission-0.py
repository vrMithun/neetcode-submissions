class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        current=[]
        result=[]
        mydict={"(":n,")":n}
        def validate(mylist):
            stack=[]
            for i in mylist:
                if not stack:
                    stack.append(i)
                elif stack[-1]=="(" and i==")":
                    stack.pop()
                else:
                    stack.append(i)
            if stack:
                return False
            return True
        def backtrack():
            if mydict["("]==0 and mydict[")"]==0:
                if validate(current):
                    result.append("".join(current.copy()))
                return
            if mydict["("]!=0:
                current.append("(")
                mydict["("]-=1
                backtrack()
                current.pop()
                mydict["("]+=1
            if mydict[")"]!=0:
                current.append(")")
                mydict[")"]-=1
                backtrack()
                current.pop()
                mydict[")"]+=1
        backtrack()
        return result
            