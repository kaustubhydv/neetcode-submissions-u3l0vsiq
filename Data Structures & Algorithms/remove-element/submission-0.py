class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = []
        for i in range(len(nums)):
            if nums[i] != val:
                ans.append(nums[i])
        nums[:] = ans
        return len(ans)
        