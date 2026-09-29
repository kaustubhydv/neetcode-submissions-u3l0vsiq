class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        res = 0

        def dfs(r, c, ):
            grid[r][c] = "0"
            dirs = [[0,1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in dirs:
                newr = r+dr
                newc = c+dc
                if min(newr, newc) < 0 or newr >= R or newc >= C or grid[newr][newc] == "0":
                    continue
                else:
                    dfs(newr, newc)

        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res
        
                
        