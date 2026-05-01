class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        window = {}
        L, length = 0, 1
        for R in range(len(s)):
            if s[R] in window:
                while s[R] in window:
                    window.pop(s[L])
                    L += 1
            length = max(length, R-L+1)
            window[s[R]] = R
        return length
        