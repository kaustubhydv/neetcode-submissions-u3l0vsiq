class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights)-1
        res = 0
        while L < R:
            if heights[L] < heights[R]:
                res = max(res, (R-L)*heights[L])
                L += 1
            else:
                res = max(res, (R-L)*heights[R])
                R -= 1
        return res

        