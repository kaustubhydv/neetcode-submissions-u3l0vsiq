class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        total = 0
        prefix = []
        for i in range(len(nums)):
            total += nums[i]
            prefix.append(total)
        for j in range(len(nums)):
            if j == 0:
                if prefix[-1] - nums[0] == 0:
                    return 0
                else:
                    continue
            if prefix[j-1] == prefix[-1] - prefix[j]:
                return j
        return -1
        
        