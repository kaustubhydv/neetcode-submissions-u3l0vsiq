class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        max_area = 0
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        def dfs(grid, r, c, area):
            if min(r,c) < 0 or r >= row or c >= col or grid[r][c] == 0:
                return area
            area += 1
            grid[r][c] = 0
            for dr, dc in dirs:
                area = dfs(grid, r+dr, c+dc, area)
            return area
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    max_area = max(dfs(grid, i, j, 0), max_area)
        return max_area
            
        