class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for val in nums:
            if val not in mp:
                mp[val] = 1
            else:
                mp[val] += 1
        res = [0]*k
        return sorted(mp, key=mp.get, reverse=True)[:k]




        