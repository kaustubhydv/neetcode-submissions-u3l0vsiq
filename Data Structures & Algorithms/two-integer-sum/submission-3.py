class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {}
        for i in range(len(nums)):
            sumMap[nums[i]] = i
        for i in range(len(nums)):
            comp = target-nums[i]
            if comp in sumMap and sumMap[comp] != i:
                return [i, sumMap[comp]]
        return []



        