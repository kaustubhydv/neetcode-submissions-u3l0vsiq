class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(i, cache):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            total1 = 0
            total1 += dfs(i+1, cache)
            total2 = nums[i]
            total2 += dfs(i+2, cache)
            cache[i] = max(total1, total2)
            return cache[i]
        return dfs(0, {})

        