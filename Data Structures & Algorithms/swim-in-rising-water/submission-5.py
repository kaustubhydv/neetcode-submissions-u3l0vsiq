class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dirs = [[0,1], [1,0], [-1, 0], [0,-1]]
        visit = {(0,0)}
        minHeap = [(grid[0][0], (0,0))]
        while minHeap:
            e1, n1 = heapq.heappop(minHeap)
            if n1 == (N-1, N-1):
                return e1
            for r, c in dirs:
                new = (r+n1[0], c+n1[1])
                if new[0] < 0 or new[0] >= N or new[1] < 0 or new[1] >= N or new in visit:
                    continue
                if new not in visit:
                    visit.add(new)
                    heapq.heappush(minHeap, (max(grid[new[0]][new[1]], e1), new))
        return -1       

        