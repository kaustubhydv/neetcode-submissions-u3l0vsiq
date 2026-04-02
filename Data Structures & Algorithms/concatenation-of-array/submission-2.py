class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums[:]
        for value in nums:
            ans.append(value)
        return ans