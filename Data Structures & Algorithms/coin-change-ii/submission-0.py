class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, currA):
            if (i, currA) in memo:
                return memo[(i, currA)]
            if i == len(coins) or currA > amount:
                return 0
            if currA == amount:
                return 1
            memo[(i, currA)] = dfs(i, currA + coins[i]) + dfs(i+1, currA)
            return memo[(i, currA)]
        return dfs(0, 0)
        