import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for val in nums:
            self.heap.append(-val)
        heapq.heapify(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        temp = self.heap[:]
        for i in range(self.k):
            if i == self.k - 1:
                return -heapq.heappop(temp)
            heapq.heappop(temp)


        
