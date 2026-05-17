class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for num in nums:
            nextPerm = []
            for p in perms:
                for i in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(i, num)
                    nextPerm.append(pCopy)
            perms = nextPerm
        return perms



        

        