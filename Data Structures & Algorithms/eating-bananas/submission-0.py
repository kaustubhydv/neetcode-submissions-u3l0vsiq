class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        time = 0
        low, high = 1, max(piles)
        arr = []
        while low <= high:
            k = (low + high)//2
            for val in piles:
                time += (val + k - 1)//k
            if time > h:
                low = k + 1
            else:
                high = k - 1
                arr.append(k)
            time = 0
        return min(arr)
        