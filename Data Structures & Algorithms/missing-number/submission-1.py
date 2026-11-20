class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumV = n*(n+1)//2
        return sumV - sum(nums)
