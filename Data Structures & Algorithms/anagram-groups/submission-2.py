class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for val in strs:
            new  = [0]*26
            for ch in val:
                temp = ord(ch) - ord('a')
                new[temp] += 1
            res[tuple(new)].append(val)
        return list(res.values())



            

       






            

        
        