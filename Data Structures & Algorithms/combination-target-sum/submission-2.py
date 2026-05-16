class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subset = []
        res = []
        def dfs(i, currSum):
            if i >= len(nums):
                return
            if currSum > target:
                return
            if currSum == target:
                res.append(subset.copy())
                return
            subset.append(nums[i])
            currSum += nums[i]
            dfs(i, currSum)
            subset.pop()
            currSum -= nums[i]
            dfs(i+1, currSum)
        dfs(0, 0)
        return res
            


                
            
        