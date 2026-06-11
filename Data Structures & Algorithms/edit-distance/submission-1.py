class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = list(range(m + 1))
        for i in range(n):
            curr = [0]*(m+1)
            curr[0] = i + 1
            for j in range(m):
                if word2[i] == word1[j]:
                    curr[j+1] = dp[j]
                else:
                    curr[j+1] = 1 + min(dp[j], dp[j+1], curr[j])
            dp = curr
        return dp[m]
