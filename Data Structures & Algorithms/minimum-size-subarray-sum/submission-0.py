class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length, L, currSum = len(nums)+1, 0, 0
        for R in range(len(nums)):
            currSum += nums[R]
            while currSum >= target:
                length = min(length, R-L+1)
                currSum -= nums[L]
                L += 1
        return 0 if length == len(nums)+1 else length

            
        