class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return (i+1, j)
        l1, r1 = 0, 1
        for i in range(len(s)):
            l,r = helper(i,i)
            if r1 - l1 < r-l:
                l1, r1 = l, r
            l,r = helper(i,i+1)
            if r1 - l1 < r-l:
                l1, r1 = l, r
        return s[l1:r1]
