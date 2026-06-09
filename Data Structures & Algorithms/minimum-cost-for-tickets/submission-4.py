class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(days):
                return 0
            memo[i] = costs[0] + dfs(i+1)
            j = i
            while j < len(days) and days[j] <= days[i]+6:
                j += 1
            memo[i] = min(memo[i], costs[1] + dfs(j))
            j = i
            while j < len(days) and days[j] <= days[i]+29:
                j += 1
            memo[i] = min(memo[i], costs[2] + dfs(j))
            return memo[i]
        return dfs(0)

        