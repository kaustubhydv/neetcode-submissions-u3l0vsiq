class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_count = 0
        max_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                curr_count = 0
                curr_count -= 1
            curr_count += 1
            max_count = max(curr_count, max_count)
        return max_count