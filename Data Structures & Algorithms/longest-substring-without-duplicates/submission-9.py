class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        res = 1
        l = 0
        visit = set()
        for i in range(len(s)):
            if s[i] in visit:
                while s[i] in visit:
                    visit.remove(s[l])
                    l += 1
            visit.add(s[i])
            res = max(res, i-l+1) 
        return res

            