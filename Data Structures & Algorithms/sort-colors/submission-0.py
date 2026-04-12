class Solution:
    def sortColors(self, nums: List[int]) -> None:
        arr = [0]*3
        for i in range(len(nums)):
            arr[nums[i]] += 1
        i = 0
        for j in range(len(arr)):
            for _ in range(arr[j]):
                nums[i] = j
                i += 1
        return nums
        