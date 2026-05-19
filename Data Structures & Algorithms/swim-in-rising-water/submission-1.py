class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if not grid or len(grid[0]) == 0:
            return -1
        adjL = defaultdict(list)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i+1 < len(grid):
                    adjL[(i,j)].append(((i+1, j), grid[i+1][j]))
                if j+1 < len(grid[0]):
                    adjL[(i,j)].append(((i, j+1), grid[i][j+1]))
                if i-1 >= 0:
                    adjL[(i,j)].append(((i-1, j), grid[i-1][j]))
                if j-1 >= 0:
                    adjL[(i,j)].append(((i, j-1), grid[i][j-1]))
        shortest = {}
        minHeap = [(grid[0][0], (0,0))]
        while (len(grid)-1, len(grid[0])-1) not in shortest:
            e1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = e1
            for n2, e2 in adjL[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (max(e2, e1), n2))
        return shortest[(len(grid)-1, len(grid[0])-1)]
        

        