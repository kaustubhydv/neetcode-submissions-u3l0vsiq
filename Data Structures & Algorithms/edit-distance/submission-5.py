class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [0]*(m+1)
        curr = [0]*(m+1)
        for j in range(m+1):
            dp[j] = j
        curr = dp
        for i in range(n):
            curr = [0]*(m+1)
            curr[0] = i+1
            for j in range(m):
                curr[j+1] = dp[j] if word1[j] == word2[i] else 1 + min(dp[j], dp[j+1], curr[j])
            dp = curr
        return curr[m]

