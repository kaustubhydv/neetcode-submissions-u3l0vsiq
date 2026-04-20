class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = [-s for s in stones]
        heapq.heapify(self.heap)
        while len(self.heap) > 1:
            curr = heapq.heappop(self.heap) - heapq.heappop(self.heap)
            if curr != 0:
                heapq.heappush(self.heap, curr)
            print(self.heap)
        if len(self.heap) < 1:
            return 0
        else:
            return -self.heap[0]

        

            



        