class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pre, suff = [0]*(n+1), [0]*(n+1)
        total = 0
        for i in range(1, n+1):
            total += nums[i-1]
            pre[i] = total
        total = 0
        for i in range(n-1, -1, -1):
            total += nums[i]
            suff[i] = total
        for i in range(1, n+1):
            if pre[i-1] == suff[i]:
                return i-1
        return -1
                


        