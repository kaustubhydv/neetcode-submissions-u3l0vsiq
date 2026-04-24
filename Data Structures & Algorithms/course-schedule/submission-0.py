class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 1:
            return True
        newMap = {}
        for i in range(numCourses):
            newMap[i] = []
        for val in prerequisites:
            newMap[val[0]].append(val[1])
        visit = set()
        def dfs(node):
            if node in visit:
                return False
            if newMap[node] == []:
                return True
            visit.add(node)
            for val in newMap[node]:
               if not dfs(val):
                return False
            visit.remove(node)
            newMap[node] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


        