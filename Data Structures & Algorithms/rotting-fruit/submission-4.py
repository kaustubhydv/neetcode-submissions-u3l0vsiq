class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dirs = [[0,1], [0, -1], [1, 0], [-1, 0]]
        q = deque()
        fresh = set()
        time = 0

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh.add((i, j))

        if not fresh:
            return time
        
        while q:
            for _ in range(len(q)):
                currR, currC = q.popleft()
                for dr, dc in dirs:
                    newR = currR + dr
                    newC = currC + dc
                    if min(newR, newC) < 0 or newR >= R or newC >= C or grid[newR][newC] != 1:
                        continue
                    else:
                        q.append((newR, newC))
                        grid[newR][newC] = 2
                        fresh.remove((newR, newC))
            time += 1
            if not fresh:
                return time
        return -1
        