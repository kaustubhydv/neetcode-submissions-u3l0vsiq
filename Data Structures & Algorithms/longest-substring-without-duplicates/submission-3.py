class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        cha = set()
        for i in range(len(s)):
            length = 0
            cha = set()
            for j in range(i, len(s)):
                if s[j] in cha:
                    break
                cha.add(s[j])
                length += 1
            res = max(length, res)
        return res
        