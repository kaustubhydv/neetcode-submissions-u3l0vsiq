class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax , globMin = nums[0], nums[0]
        currMax, currMin, total = 0, 0, 0
        for n in nums:
            currMax = max(currMax, 0) + n
            currMin = min(currMin, 0) + n
            total += n
            globMax = max(currMax, globMax)
            globMin = min(currMin, globMin)
        return max(globMax, total - globMin) if globMax > 0 else globMax
        


        