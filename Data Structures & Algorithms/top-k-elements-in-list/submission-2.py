class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for val in nums:
            if val in count:
                count[val] += 1
            else:
                count[val] = 1
        heap = []
        for val in count.keys():
            heapq.heappush(heap, (count[val], val))
            while len(heap) > k:
                heapq.heappop(heap)
        res = []
        for c, key in heap:
            res.append(key)
        return res
        
        
        