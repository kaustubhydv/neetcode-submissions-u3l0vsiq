class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indegree = [0]*numCourses
        adjL = {i:[] for i in range(numCourses)}
        isPreReq = {i:set() for i in range(numCourses)}
        for pre, nxt in prerequisites:
            adjL[pre].append(nxt)
            indegree[nxt] += 1
        q = deque(i for i in range(numCourses) if indegree[i] == 0)
        while q:
            node = q.popleft()
            for n in adjL[node]:
                indegree[n] -= 1
                isPreReq[n].add(node)
                isPreReq[n].update(isPreReq[node])
                if indegree[n] == 0:
                    q.append(n)
        return [u in isPreReq[v] for u,v in queries]
        
        