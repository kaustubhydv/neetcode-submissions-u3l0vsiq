class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        temp = 0
        for val in nums:
            if val == 1:
                temp += 1
                maxCount = max(temp, maxCount)
            else:
                temp = 0
        return maxCount

        