class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0] * 3

        for i in nums:
            count[i] += 1
        
        k = 0
        for i in range(3):
            for j in range(count[i]):
                nums[k] = i
                k += 1
        