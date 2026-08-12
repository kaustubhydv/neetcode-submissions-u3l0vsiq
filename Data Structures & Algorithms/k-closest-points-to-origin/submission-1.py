class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, (x, y) in enumerate(points):
            dist = math.sqrt(x**2 + y**2)
            heap.append((-dist, i))
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        res = []
        for dist, i in heap:
            res.append(points[i])
        return res




        