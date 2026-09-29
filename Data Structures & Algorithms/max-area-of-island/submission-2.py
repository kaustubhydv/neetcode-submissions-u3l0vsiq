class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        resA = 0

        def dfs(r, c):
            count = 1
            grid[r][c] = 0
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in dirs:
                newr = r+dr
                newc = c+dc
                if min(newr, newc) < 0 or newr >= R or newc >= C or grid[newr][newc] == 0:
                    continue
                else:
                    count += dfs(newr, newc)
            return count
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    resA = max(resA, dfs(r, c)) 
        return resA
        
            

        