class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        i = 2
        dp = [0, 1]
        while i <= n+1:
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp
            i += 1
        return dp[1]
        