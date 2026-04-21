class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        islands = 0
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(grid, r, c):
            if min(r,c) < 0 or r >= row or c >= col or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for dr, dc in dirs:
                dfs(grid, r+dr, c+dc)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    islands += 1
        return islands
            

        