class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]
        for val in nums:
            currSum = max(currSum, 0)
            currSum += val
            maxSum = max(maxSum, currSum)
        return maxSum
        