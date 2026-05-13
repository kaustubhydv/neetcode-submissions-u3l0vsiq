class Solution:
    def unionFind(self, n):
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
        p1, p2 = self.par[n1], self.par[n2]
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

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = self.unionFind(len(accounts))
        emailAcc = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailAcc:
                    self.union(i, emailAcc[e])
                else:
                    emailAcc[e] = i

        email = defaultdict(list)
        for key, val in emailAcc.items():
            par = self.find(val)
            email[par].append(key)
        res = []
        for key, val in email.items():
            name = accounts[key][0]
            res.append([name] + sorted(email[key]))
        return res



        