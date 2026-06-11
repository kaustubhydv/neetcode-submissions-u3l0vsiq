class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == m:
                memo[(i, j)] = n-j
                return memo[(i, j)]
            if j == n:
                memo[(i, j)] = m-i
                return memo[(i, j)]
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i+1, j+1)
            else:
                memo[(i, j)] = 1 + min(dfs(i+1, j+1), dfs(i, j+1), dfs(i+1, j))
            return memo[(i, j)]
        return dfs(0,0)


        