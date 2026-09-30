class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adjL = {}
        for i in range(n):
            adjL[i] = []
        for x, y in edges:
            adjL[x].append(y)
            adjL[y].append(x)
        q = deque()
        visit = set()
        q.append(0)
        visit.add(0)
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for nei in adjL[curr]:
                    if nei not in visit:
                        q.append(nei)
                        visit.add(nei)
        return len(visit) == n