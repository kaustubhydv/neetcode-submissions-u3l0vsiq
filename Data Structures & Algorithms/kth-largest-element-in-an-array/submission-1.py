class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k<=0:
            return None
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]

        