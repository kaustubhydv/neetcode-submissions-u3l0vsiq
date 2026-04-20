class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            if abs(stones[-1] - stones[-2]) != 0:
                x, y = stones[-1], stones[-2]
                stones.pop()
                stones.pop()
                stones.append(abs(x-y))
            else:
                stones.pop()
                stones.pop()
        if len(stones) == 0:
            return 0
        else:
            return stones[0]

            



        