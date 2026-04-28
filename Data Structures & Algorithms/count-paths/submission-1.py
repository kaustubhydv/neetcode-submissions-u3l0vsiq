class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = []
        for _ in range(m):
            cache.append([0]*n)
        def topDown(r,c, cache):
            if r == m or c == n:
                return 0
            if cache[r][c]:
                return cache[r][c]
            if r == m-1 or c == n-1:
                return 1
            cache[r][c] = topDown(r+1,c, cache) + topDown(r,c+1, cache)
            return cache[r][c]
        return topDown(0,0,cache)
        