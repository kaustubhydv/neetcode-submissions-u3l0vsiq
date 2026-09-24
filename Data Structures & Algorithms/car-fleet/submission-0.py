class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        visit = []
        n = len(position)
        for i in range(len(position)):
            visit.append((position[i], speed[i]))
        visit.sort(reverse=True)
        stack = []
        for i in range(n):
            stack.append((target-visit[i][0])/visit[i][1])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        