class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0]*n
        total = 0
        hashMap = {0 : 1}
        res = 0
        for i in range(n):
            total += nums[i]
            pre[i] = total
        for i in range(n):
            if pre[i] - k in hashMap:
                res += hashMap[pre[i] - k]
            if pre[i] in hashMap:
                hashMap[pre[i]] += 1
            else:
                hashMap[pre[i]] = 1
        return res
        