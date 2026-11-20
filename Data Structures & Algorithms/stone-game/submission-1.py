class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            al = (r-l) % 2 == 1
            left = piles[l] if al else 0
            right = piles[r] if al else 0
            dp[(l, r)] = max(dfs(l+1, r) + left, dfs(l, r-1) + right)
            return dp[l, r]
        total = sum(piles)
        alice = dfs(0, len(piles)-1)
        return True if alice > total/2 else False
        
        