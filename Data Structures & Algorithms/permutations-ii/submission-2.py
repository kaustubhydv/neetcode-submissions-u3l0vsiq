class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        subset = []
        visit = set()
        nums.sort()
        def dfs(i):
            if len(subset) == len(nums):
                res.add(tuple(subset.copy()))
                return
            if i == len(nums):
                return
            for j in range(len(nums)):
                if j in visit:
                    continue
                subset.append(nums[j])
                visit.add(j)
                dfs(i+1)
                subset.pop()
                visit.remove(j)
        dfs(0)
        return list(res)


        