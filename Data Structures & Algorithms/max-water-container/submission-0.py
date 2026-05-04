class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        for L in range(len(heights)):
            for R in range(L, len(heights)):
                maxA = max(maxA, min(heights[L], heights[R])*(R-L))
        return maxA



        


        