class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        visit = set(range(len(nums)+1))
        for n in nums:
            visit.remove(n)
        return list(visit)[0]