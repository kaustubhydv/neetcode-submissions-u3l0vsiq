class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1]:
            return -1
        queue = deque()
        visit = set()
        queue.append((0,0))
        visit.add((0,0))
        length = 1

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == n-1 and c == n-1:
                    return length
                dirs = [[1, 0], [-1,0], [0,1], [0,-1], [1,-1], [1,1], [-1,1], [-1,-1]]
                for dr,dc in dirs:
                    newr = r+dr
                    newc = c+dc
                    if (min(newr, newc) < 0 or 
                    max(newr, newc) >= n or
                    (newr, newc) in visit or
                    grid[newr][newc] == 1):
                        continue
                    queue.append((newr, newc))
                    visit.add((newr, newc))
            length += 1
        return -1



        
        