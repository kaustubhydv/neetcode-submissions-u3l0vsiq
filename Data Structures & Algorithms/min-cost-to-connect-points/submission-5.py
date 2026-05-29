class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i, (x1,y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points):
                if i != j:
                    dist = abs(x1-x2) + abs(y1-y2)
                    edges.append((dist, i, j))
        edges.sort(key=lambda e: e[0])
        res = 0
        uf = UnionFind(len(edges))
        for d, i, j in edges:
            if uf.union(i, j):
                res += d
        return res




class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, n):
        while n != self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True



        

                


        