class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        res = R
        while L <= R:
            mid = (L+R)//2
            time = 0
            for val in piles:
                time += math.ceil(val/mid)
            if time > h:
                L = mid + 1
            else:
                res = mid
                R = mid -1
        return res
        