class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        if grid:
            m, n = len(grid), len(grid[0])
        else:
            return 0
        def dfs(r, c, area):
            if min(r, c) < 0 or r == m or c == n or grid[r][c] == 0:
                return area
            area += 1
            grid[r][c] = 0
            for dr, dc in dirs:
                area = max(area, dfs(r+dr, c+dc, area))
            return area

    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(dfs(i, j, 0), maxArea)
        return maxArea
        