class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        visit = set()
        nums.sort()
        def dfs(i):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            if i == len(nums):
                return
            for j in range(len(nums)):
                if j in visit:
                    continue
                if j > 0 and nums[j] == nums[j-1] and j-1 not in visit:
                    continue 
                subset.append(nums[j])
                visit.add(j)
                dfs(i+1)
                subset.pop()
                visit.remove(j)
        dfs(0)
        return res


        