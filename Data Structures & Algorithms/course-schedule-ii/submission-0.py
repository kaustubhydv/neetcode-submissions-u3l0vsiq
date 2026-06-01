class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjL = {i: [] for i in range(numCourses)}
        for n1, n2 in prerequisites:
            adjL[n1].append(n2)
        path = set()
        visit = set()
        topSort = []
        def dfs(node):
            if node in path:
                return False
            if node in visit:
                return True
            path.add(node)
            visit.add(node)
            for n in adjL[node]:
                if not dfs(n):
                    return False
            topSort.append(node)
            path.remove(node)
            return True
        for node in adjL:
            if not dfs(node):
                return []
        return topSort

