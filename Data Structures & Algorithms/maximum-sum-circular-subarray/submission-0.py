class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        for i in range(len(nums)):
            currSum = 0
            maxSum1 = nums[i]
            for j in range(i, i+len(nums)):
                if j >= len(nums):
                    j = j % len(nums)
                currSum = max(currSum, 0) + nums[j]
                maxSum1 = max(maxSum1, currSum)
            maxSum = max(maxSum1, maxSum)
        return maxSum


        