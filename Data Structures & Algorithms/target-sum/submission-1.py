class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def dfs(i, currSum):
            if i == n:
                return 1 if currSum == target else 0
            if (i, currSum) in memo:
                return memo[(i, currSum)]
            memo[(i, currSum)] = dfs(i+1, currSum - nums[i]) + dfs(i+1, currSum + nums[i])
            return memo[(i, currSum)]
        return dfs(0, 0)