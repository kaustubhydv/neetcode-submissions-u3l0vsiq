class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = nums[:]
        ans.sort()
        for i in range(len(ans)-1):
            if ans[i] == ans[i+1]:
                return True
        return False
            
        