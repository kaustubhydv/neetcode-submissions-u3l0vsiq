class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visit = {}
        for i, val in enumerate(nums):
            if val in visit:
                return [visit[val], i]
            visit[target - val] = i
        return None