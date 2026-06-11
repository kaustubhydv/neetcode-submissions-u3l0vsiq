class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        N, M = len(text1), len(text2)
        dp = [0]*(M+1)
        for i in range(N):
            curr = [0]*(M+1)
            for j in range(M):
                curr[j+1] = 1 + dp[j] if text1[i] == text2[j] else max(dp[j+1], curr[j])
            dp = curr
        return dp[M]
