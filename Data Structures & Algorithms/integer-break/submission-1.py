class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}
        def dfs(val):
            if val in dp:
                return dp[val]
            if val <= 1:
                return 1
            res = 0 if val == n else val
            for i in range(1, (val+1)//2 + 1):
                res = max(res, i*dfs(val-i))
            dp[val] = res
            return res
        return dfs(n)