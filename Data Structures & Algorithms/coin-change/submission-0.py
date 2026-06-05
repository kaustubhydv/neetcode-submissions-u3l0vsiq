class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(i, amount, cache):
            if (i, amount) in cache:
                return cache[(i, amount)]
            if amount == 0:
                return 0
            if i == len(coins) or amount < 0:
                return float('inf')
            cache[(i, amount)] = dfs(i+1, amount, cache)
            if amount - coins[i] >= 0:
                new = 1 + dfs(i, amount - coins[i], cache)
                cache[(i, amount)] = min(cache[(i, amount)], new)
            return cache[(i, amount)]
        res = dfs(0, amount, {})
        return res if res != float('inf') else -1
        