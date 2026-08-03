class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(i, subs):
            if i == len(nums):
                res.append(subs)
                return
            helper(i+1, subs.copy())
            subs.append(nums[i])
            helper(i+1, subs.copy())
        helper(0, [])
        return res
            

        