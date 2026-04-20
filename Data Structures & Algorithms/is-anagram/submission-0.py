class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap = {}
        secCharMap = {}
        for char in s:
            if char in charMap:
                charMap[char] += 1
            else:
                charMap[char] = 1
        for char in t:
            if char in secCharMap:
                secCharMap[char] += 1
            else:
                secCharMap[char] = 1
        return charMap == secCharMap
        

        
        