class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjL = {}
        for i in range(n):
            adjL[i] = []
        for x, y in edges:
            adjL[x].append(y)
            adjL[y].append(x)
        visit = set()
        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            for nei in adjL[i]:
                dfs(nei)
            return
        count = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1
        count = count + (n - len(visit))
        return count

        