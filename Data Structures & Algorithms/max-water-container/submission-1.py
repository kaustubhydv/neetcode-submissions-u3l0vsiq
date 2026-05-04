class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        L, R = 0, len(heights) - 1
        while L < R:
            maxA = max(maxA, (R-L)*min(heights[L], heights[R]))
            if min(heights[L], heights[R]) == heights[R]:
                R -= 1
            else:
                L += 1
        return maxA



        


        