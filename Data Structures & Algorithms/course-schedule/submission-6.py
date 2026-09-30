class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjL = {}
        for i in range(numCourses):
            adjL[i] = []
        for after, pre in prerequisites:
            adjL[after].append(pre)
        path = set()
        done = set()
        def dfs(i):
            if i in done:
                return True
            if i in path:
                return False
            path.add(i)
            for n in adjL[i]:
                if not dfs(n):
                    return False
            done.add(i)
            path.remove(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

                
        