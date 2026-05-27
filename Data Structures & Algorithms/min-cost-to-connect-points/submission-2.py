class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjL = defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    adjL[tuple(points[i])].append((dist, tuple(points[j])))
        minHeap = []
        for d, p in adjL[tuple(points[0])]:
            heapq.heappush(minHeap, (d, tuple(points[0]), tuple(p)))
        res = 0
        visit = set()
        visit.add(tuple(points[0]))
        while len(visit) < len(points):
            d, n1, n2 = heapq.heappop(minHeap)
            if n2 in visit:
                continue
            visit.add(n2)
            res += d
            for d, p in adjL[n2]:
                if p not in visit:
                    heapq.heappush(minHeap, (d, n2, p))
        return res

                


        