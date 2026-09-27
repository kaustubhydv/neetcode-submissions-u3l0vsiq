class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) <= 1:
            return 0
        L, R = 0, len(heights) - 1
        maxA = 0
        while L < R:
            if heights[L] > heights[R]:
                area = (R - L)*(heights[R])
                R -= 1
            else:
                area = (R - L)*(heights[L])
                L += 1
            maxA = max(maxA, area)
        return maxA

        