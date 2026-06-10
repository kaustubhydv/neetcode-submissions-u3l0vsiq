class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        d7, d30 = deque(), deque()
        dp = 0
        for d in days:
            while d7 and d7[0][0] + 7 <= d:
                d7.popleft()
            while d30 and d30[0][0] + 30 <= d:
                d30.popleft()
            d7.append([d, dp + costs[1]])
            d30.append([d, dp + costs[2]])
            dp = min(dp+costs[0], d7[0][1], d30[0][1])
        return dp

        