class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        avail = []
        pen = []
        for i, (e, p) in enumerate(tasks):
            heapq.heappush(pen, (e, p, i))
        time = 0
        res = []
        while avail or pen:
            while pen and time >= pen[0][0]:
                e,p,i = heapq.heappop(pen)
                heapq.heappush(avail, (p,i,e))
            if not avail:
                time = pen[0][0]
                continue
            p,i,e = heapq.heappop(avail)
            time += p
            res.append(i)
        return res
            
            

        