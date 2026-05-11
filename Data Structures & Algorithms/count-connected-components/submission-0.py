class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = {}
        rank = {}
        for i in range(n):
            par[i] = i
            rank[i] = 0
        def find(node):
            while node != par[node]:
                par[node] = par[par[node]]
                node = par[node]
            return node
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p1] < rank[p2]:
                par[p1] = p2
            else:
                par[p1] = p2
                rank[p2] += 1
            return 1

        count = n
        for n1, n2 in edges:
            count -= union(n1,n2)
        return count
        

        