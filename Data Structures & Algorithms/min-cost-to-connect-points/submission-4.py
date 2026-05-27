class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjL = defaultdict(list)
        N = len(points)
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adjL[i].append((dist, j))
                adjL[j].append((dist, i))
        minHeap = [[0, 0]]
        res = 0
        visit = set()
        while len(visit) < len(points):
            d, n2 = heapq.heappop(minHeap)
            if n2 in visit:
                continue
            visit.add(n2)
            res += d
            for d, p in adjL[n2]:
                if p not in visit:
                    heapq.heappush(minHeap, (d, p))
        return res

                


        