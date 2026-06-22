class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for val in nums:
            if val in count:
                count[val] += 1
            else:
                count[val] = 1
        sort = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sort[0:k]]