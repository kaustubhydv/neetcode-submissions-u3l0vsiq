class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charMap = {}
        secCharMap = {}
        for i in range(len(s)):
            if s[i] in charMap:
                charMap[s[i]] += 1
            else:
                charMap[s[i]] = 1
            if t[i] in secCharMap:
                secCharMap[t[i]] += 1
            else:
                secCharMap[t[i]] = 1
        return charMap == secCharMap
        

        
        