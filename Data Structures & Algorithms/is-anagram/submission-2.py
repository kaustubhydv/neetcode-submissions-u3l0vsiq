class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for val in s:
            if val in hashmap:
                hashmap[val] += 1
            else:
                hashmap[val] = 1
        hashmap2 = {}
        for val in t:
            if val in hashmap2:
                hashmap2[val] += 1
            else:
                hashmap2[val] = 1
        return hashmap == hashmap2
        