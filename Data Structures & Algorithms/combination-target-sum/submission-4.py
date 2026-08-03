class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sols = []
        def helper(i):
            nonlocal target
            if target < 0 or i >= len(nums):
                return None
            if target == 0:
                res.append(sols.copy())
                return None
            target -= nums[i]
            sols.append(nums[i])
            helper(i)
            target += nums[i]
            sols.pop()
            helper(i+1)
        helper(0)
        return res
            
        