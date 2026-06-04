class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        memo = {}
        def dfs(i, currSum):
            if i == len(stones):
                return abs(currSum)
            if (i, currSum) in memo:
                return memo[(i, currSum)]
            currSum += stones[i]
            res = dfs(i+1, currSum)
            currSum = currSum - 2*stones[i]
            res = min(res, dfs(i+1, currSum))
            currSum += stones[i]
            memo[(i, currSum)] = res
            return res
        return dfs(0, 0)

            
            
            



