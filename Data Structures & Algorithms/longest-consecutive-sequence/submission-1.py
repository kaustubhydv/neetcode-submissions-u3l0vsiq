class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        res = 0 if len(nums) == 0 else 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                count += 1
                res = max(count, res)
            else:
                count = 1
        return res
        