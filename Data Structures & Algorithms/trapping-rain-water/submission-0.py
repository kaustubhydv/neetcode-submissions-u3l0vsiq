class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        for L in range(1, len(height)-1):
                currA = min(max(height[:L]), max(height[L+1:])) - height[L]
                if currA > 0:
                    area += currA
        return area
            
        