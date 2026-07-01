class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        maxL = 0
        for val in lookup:
            curr = val
            res = 1
            while curr + 1 in lookup:
                res += 1
                curr += 1
            maxL = max(res, maxL)
        return maxL

        
        
        