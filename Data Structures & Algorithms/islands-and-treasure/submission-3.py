class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        dirs = [[0,1], [0, -1], [1, 0], [-1, 0]]
        q = deque()

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        while q:
            for _ in range(len(q)):
                currR, currC = q.popleft()
                for dr, dc in dirs:
                    newR = currR + dr
                    newC = currC + dc
                    if min(newR, newC) < 0 or newR >= R or newC >= C or grid[newR][newC] != 2147483647:
                        continue
                    else:
                        grid[newR][newC] = grid[currR][currC] + 1
                        q.append((newR, newC))
        
