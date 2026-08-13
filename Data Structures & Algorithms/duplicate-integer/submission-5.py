class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visit = set()
        for val in nums:
            if val in visit:
                return True
            visit.add(val)
        return False
        