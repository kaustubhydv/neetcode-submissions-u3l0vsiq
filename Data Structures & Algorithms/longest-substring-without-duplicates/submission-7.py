class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            count = 0
            visit = set()
            for j in range(i, len(s)):
                if s[j] not in visit:
                    count += 1
                    res = max(res, count)
                    visit.add(s[j])
                else:
                    break
        return res



        