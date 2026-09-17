class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val = {}
        for n in nums:
            if n in val:
                val[n] += 1
            else:
                val[n] = 0
        arr = []
        for n, freq in val.items():
            arr.append([freq, n])
        arr.sort(reverse=True)
        res = []
        i = 0
        while len(res) < k:
            res.append(arr[i][1])
            i += 1
        return res
            

        

        