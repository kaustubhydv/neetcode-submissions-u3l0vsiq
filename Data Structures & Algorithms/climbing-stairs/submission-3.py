class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        arr = [1,1]
        i = 2
        while i <= n:
            arr[0], arr[1] = arr[1], arr[0] + arr[1]
            i += 1
        return arr[1]
