import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-p for p in stones]
        while len(arr) > 1:
            heapq.heapify(arr)
            st1 = heapq.heappop(arr)
            st2 = heapq.heappop(arr)
            if st1 == st2:
                continue
            else:
                heapq.heappush(arr, -abs(st1-st2))
        return 0 if not arr else -arr[0]


        