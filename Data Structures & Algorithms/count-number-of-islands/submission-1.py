class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m, n = len(grid), len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(i, j, m, n, grid)
        return count
    def dfs(self, r, c, m, n, grid):
            if min(r, c) < 0 or r == m or c == n or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in dirs:
                self.dfs(r+dr, c+dc, m, n, grid)



        