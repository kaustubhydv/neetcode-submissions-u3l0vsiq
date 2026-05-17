class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums) == 1:
            return [[nums[0]]]
        def backtrack(i):
            if i == len(nums)-1:
                return [[nums[i]]]
            perms = backtrack(i+1)
            nextPerm = []
            for p in perms:
                for j in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    nextPerm.append(pCopy)
            return nextPerm
        return backtrack(0)



        

        