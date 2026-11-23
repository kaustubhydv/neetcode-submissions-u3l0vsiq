class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        def dfs(i, currDay):
            if (i, currDay) in memo:
                return memo[(i, currDay)]
            if i == len(days):
                memo[(i, currDay)] = 0
                return 0
            if currDay >= days[i]:
                memo[(i, currDay)] = dfs(i+1, currDay)
                return memo[(i, currDay)]
            memo[(i, currDay)] = min(
            costs[0] + dfs(i+1, days[i]),
            costs[1] + dfs(i+1, days[i]+6),
            costs[2] + dfs(i+1, days[i]+29)
            )
            return memo[(i, currDay)]
        return dfs(0, 0)
        