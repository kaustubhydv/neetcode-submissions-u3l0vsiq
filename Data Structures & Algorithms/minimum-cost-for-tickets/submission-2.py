class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        def dfs(i, day):
            if (i, day) in memo:
                return memo[(i, day)]
            if i==len(days):
                return 0
            if days[i] <= day:
                return dfs(i+1, day)
            res1 = costs[0] + dfs(i+1, days[i])
            res7 = costs[1] + dfs(i+1, days[i]+6)
            res30 = costs[2] + dfs(i+1, days[i]+29)
            memo[(i, day)] = min(res1, res7, res30)
            return memo[(i, day)]
        return dfs(0, 0)

        