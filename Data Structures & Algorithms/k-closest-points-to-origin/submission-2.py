import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            arr.append((-dist, x, y))
        heapq.heapify(arr)
        while len(arr) > k:
            heapq.heappop(arr)
        res = []
        for d, x, y in arr:
            res.append([x, y])
        return res

