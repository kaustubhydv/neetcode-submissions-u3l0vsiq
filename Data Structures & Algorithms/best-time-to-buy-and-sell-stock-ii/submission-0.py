class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = None
        maxProfit = 0
        cache = {}
        def dfs(i, bought):
            if i >= len(prices):
                return 0
            if (i, bought) in cache:
                return cache[(i, bought)]
            profit = dfs(i+1, bought)
            if not bought and bought != 0:
                curr = -prices[i]
                curr = max(profit, curr + dfs(i+1, i))
            else:
                curr = prices[i]
                curr = max(profit, curr + dfs(i+1, None))
            cache[(i, bought)] = curr
            return curr
        return dfs(0, None)
                
            
            
            

        