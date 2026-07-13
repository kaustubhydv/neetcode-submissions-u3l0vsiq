class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        res = 1
        l, r = 0, 0
        visit = set(s[l:r+1])
        for i in range(r+1, len(s)):
            if s[i] in visit:
                while s[i] in visit:
                    visit.remove(s[l])
                    l += 1
            visit.add(s[i])
            r += 1
            res = max(res, r-l+1) 
        return res

            