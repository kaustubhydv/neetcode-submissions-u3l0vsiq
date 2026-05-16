class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        subset = []
        res = []
        def dfs(i):
            if len(subset) == k:
                res.append(subset.copy())
                return
            for j in range(i, n+1):
                subset.append(j)
                dfs(j+1)
                subset.pop()
        dfs(1)
        return res
        