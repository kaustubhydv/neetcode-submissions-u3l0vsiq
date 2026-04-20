class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap = {}
        for val in nums:
            if val in countMap:
                return True
            else:
                countMap[val] = 0
        return False
            
        