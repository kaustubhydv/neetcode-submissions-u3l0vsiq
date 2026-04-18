class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def backtrack(i, current_sum):
            if i >= len(nums) or current_sum > target:
                return
            if current_sum == target:
                res.append(subset[:])
                return
            subset.append(nums[i])
            backtrack(i, current_sum + nums[i])
            subset.pop()
            backtrack(i+1, current_sum)
        backtrack(0, 0)
        return res


                
            
        