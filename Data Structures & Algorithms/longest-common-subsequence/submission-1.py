class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        def dfs(i,j, cache):
            if i == m or j==n:
                return 0
            if cache[i][j]:
                return cache[i][j]
            if text1[i] == text2[j]:
                cache[i][j] = 1+dfs(i+1, j+1, cache)
            else:
                cache[i][j] = max(dfs(i+1, j, cache), dfs(i, j+1, cache))
            return cache[i][j]
        return dfs(0,0, [[0]*(n+1) for _ in range(m+1)])
        