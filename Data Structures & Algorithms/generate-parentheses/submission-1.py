class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        current = []
        result = []

        def backtrack(open, close):

            if open == 0 and close == 0:
                result.append("".join(current))
                return

            if open > 0:
                current.append("(")
                backtrack(open - 1, close)
                current.pop()

            if close > open:
                current.append(")")
                backtrack(open, close - 1)
                current.pop()

        backtrack(n, n)

        return result