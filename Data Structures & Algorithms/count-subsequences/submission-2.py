class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(t), len(s)
        dp = [1]*(n+1)
        for i in range(m):
            curr = [0]*(n+1)
            for j in range(n):
                curr[j+1] = curr[j]
                if s[j] == t[i]:
                    curr[j+1] += dp[j]
            dp = curr
        return dp[n]