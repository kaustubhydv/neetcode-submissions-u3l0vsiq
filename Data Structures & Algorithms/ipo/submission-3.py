class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []
        minCap = []
        for i in range(len(profits)):
            minCap.append((capital[i], profits[i]))
        heapq.heapify(minCap)
        for _ in range(k):
            while minCap and minCap[0][0] <= w:
                c,p = heapq.heappop(minCap)
                heapq.heappush(maxProfit, -p)
            if not maxProfit:
                break
            w -= heapq.heappop(maxProfit)
        return w
                    


        
        