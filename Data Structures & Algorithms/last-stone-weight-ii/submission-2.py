class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        memo = {}
        total = sum(stones)
        target = total//2
        def dfs(i, currSum):
            if i == len(stones) or currSum >= target:
                return abs(total - 2*currSum )
            if (i, currSum) in memo:
                return memo[(i, currSum)]
            memo[(i, currSum)] = min(dfs(i+1, currSum), dfs(i+1, currSum+stones[i]))
            return memo[(i, currSum)]
        return dfs(0, 0)

            
            
            



