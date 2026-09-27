class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        L, R = 0, 1
        while R <= len(nums) - 1:
            if nums[L] == nums[R]:
                R += 1
                continue
            else:
                L += 1
                nums[L] = nums[R]
                R += 1
        return L+1

        