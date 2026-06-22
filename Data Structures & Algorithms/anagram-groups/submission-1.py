class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for val in strs:
            sortedS = ''.join(sorted(val))
            res[sortedS].append(val)
        return list(res.values())



            

       






            

        
        