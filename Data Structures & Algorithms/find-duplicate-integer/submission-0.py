class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visit = set()
        for val in nums:
            if val in visit:
                return val
            visit.add(val)
        