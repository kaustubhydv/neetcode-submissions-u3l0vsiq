class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i < 0 or j >= len(s) or i > j:
                return 0
            if s[i] == s[j]:
                length = 1 if i == j else 2
                memo[(i, j)] = length + dfs(i-1, j+1)
            else:
                memo[(i, j)] = max(dfs(i, j+1), dfs(i-1, j))
            return memo[(i, j)]
        res = 0
        for i in range(len(s)):
            res = max(res, dfs(i, i))
            res = max(res, dfs(i, i+1))
        return res
        
        