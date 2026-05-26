class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjL = defaultdict(list)
        for i in range(len(edges)):
            adjL[edges[i][0]].append((edges[i][1], succProb[i]))
            adjL[edges[i][1]].append((edges[i][0], succProb[i]))
        visit = set()
        maxHeap = [(-1, start_node)]
        while maxHeap:
            prob, node = heapq.heappop(maxHeap)
            visit.add(node)
            if node == end_node:
                return -prob
            for node1, prob1 in adjL[node]:
                if node1 not in visit:
                    heapq.heappush(maxHeap, (prob1*prob, node1))
        return 0

        

        