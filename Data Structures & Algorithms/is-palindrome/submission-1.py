class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","")
        s=s.lower()
        for i in s:
            if not i.isalnum():
                s=s.replace(i,"")
        if s==s[::-1]:
            return True
        return False