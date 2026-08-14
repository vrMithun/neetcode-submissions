class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()
        left = 0
        right = 0
        result = 0

        while right < len(s):
            if s[right] not in myset:
                myset.add(s[right])
                result = max(result, right - left + 1)
                right += 1

            else:
                myset.remove(s[left])
                left += 1

        return result