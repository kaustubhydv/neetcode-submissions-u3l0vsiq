class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visit = {}
        for i in range(len(nums)):
            if target - nums[i] in visit and i != visit[target - nums[i]]:
                return [visit[target - nums[i]], i]
            visit[nums[i]] = i
        return []


        