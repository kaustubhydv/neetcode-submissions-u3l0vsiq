class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N, M = len(coins), amount+1
        prevRow, currRow = [0]*M, [0]*M
        for i in range(N):
            currRow[0] = 1
            for j in range(M):
                if j >= coins[i]:
                    currRow[j] = prevRow[j]
                    currRow[j] += currRow[j-coins[i]]
                prevRow = currRow
        return prevRow[M-1]

        