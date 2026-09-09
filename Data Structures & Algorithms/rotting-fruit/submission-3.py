class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        m, n = len(grid), len(grid[0])
        time = -1
        dirs = [[0,1], [1,0], [0,-1], [-1, 0]]
        fresh = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh.add((i, j))
        if not fresh:
            return 0
        while len(queue) > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if min(nr, nc) < 0 or nr >= m or nc >= n or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    fresh.remove((nr, nc))

                    queue.append((nr, nc))
            time += 1
        return time if not fresh else -1