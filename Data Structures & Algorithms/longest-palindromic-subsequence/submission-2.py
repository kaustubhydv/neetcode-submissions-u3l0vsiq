class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                memo[(i, j)] = 2 + dfs(i+1, j-1)
            else:
                memo[(i, j)] = max(dfs(i, j-1), dfs(i+1, j))
            return memo[(i, j)]
        return dfs(0, len(s)-1)
        
        