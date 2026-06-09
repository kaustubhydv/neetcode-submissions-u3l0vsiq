class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(days):
                return 0
            res1 = costs[0] + dfs(i+1)
            j = i
            while j < len(days) and days[j] <= days[i]+6:
                j += 1
            res7 = costs[1] + dfs(j) 
            j = i
            while j < len(days) and days[j] <= days[i]+29:
                j += 1
            res30 = costs[2] + dfs(j) 
            memo[i] = min(res1, res7, res30)
            return memo[i]
        return dfs(0)

        