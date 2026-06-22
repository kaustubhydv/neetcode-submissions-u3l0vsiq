class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for val in nums:
            if val in count:
                count[val] += 1
            else:
                count[val] = 1
        freq = [[] for _ in range(len(nums)+1)]
        for num, count in count.items():
            freq[count].append(num)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for val in freq[i]:
                res.append(val)
            if len(res) == k:
                return res

        
        
        