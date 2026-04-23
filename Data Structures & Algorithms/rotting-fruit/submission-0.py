class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        time = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i,j))
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                dirs = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in dirs:
                    newr = r+dr
                    newc = c+dc
                    if (newr in range(len(grid))
                        and newc in range(len(grid[0]))
                        and grid[newr][newc] == 1
                    ):
                        grid[newr][newc] = 2
                        queue.append((newr, newc))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1


                

