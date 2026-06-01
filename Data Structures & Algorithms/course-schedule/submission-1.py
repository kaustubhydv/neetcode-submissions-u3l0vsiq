class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjL = {}
        for i in range(numCourses):
            adjL[i] = []
        for n1, n2 in prerequisites:
            adjL[n1].append(n2)
        visit = set()
        path = set()
        def dfs(node):
            if node in path:
                return False
            if node in visit:
                return True
            visit.add(node)
            path.add(node)
            for n in adjL[node]:
                if not dfs(n):
                    return False
            path.remove(node)
            return True
        for node in adjL:
            if not dfs(node):
                return False
        return True

        


        