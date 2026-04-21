class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        length = 0
        visited.add((0,0))
        queue.append((0,0))
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == row-1 and c == col-1:
                    return length
                dirs = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr,dc in dirs:
                    newr = r+dr
                    newc = c+dc
                    if (min(newr,newc) < 0 or 
                    newr >= row or 
                    newc >= col or 
                    (newr, newc) in visited or
                    grid[newr][newc] == 1):
                        continue
                    queue.append((newr, newc))
                    visited.add((newr, newc))
            length += 1
        return -1



        