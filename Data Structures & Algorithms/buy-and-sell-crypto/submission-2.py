class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]
        for p in prices:
            buy = min(p, buy)
            maxProfit = max(p - buy, maxProfit)
        return maxProfit






        