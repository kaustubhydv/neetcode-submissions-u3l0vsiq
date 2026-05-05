class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        prefix = {0: 1}
        count = 0
        for i in range(len(nums)):
            total += nums[i]
            diff = total - k
            count += prefix.get(diff, 0)
            prefix[total] = 1 + prefix.get(total, 0)
        return count



        