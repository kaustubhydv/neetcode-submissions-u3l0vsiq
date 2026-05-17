class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = []
        visit = set()
        def dfs(i):
            if len(nums) == len(subset):
                res.append(subset.copy())
            if i == len(nums):
                return
            for j in range(len(nums)):
                if j in visit:
                    continue
                visit.add(j)
                subset.append(nums[j])
                dfs(i+1)
                visit.remove(j)
                subset.pop()
        dfs(0)
        return res

        