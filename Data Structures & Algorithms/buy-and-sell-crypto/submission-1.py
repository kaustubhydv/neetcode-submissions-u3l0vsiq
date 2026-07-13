class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0
        for p in prices:
            buy = min(p, buy)
            res = max(0, max(p, res + buy) - buy)
        return res



        