"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visit = {}
        def dfs(n):
            if not n:
                return None
            if n in visit:
                return visit[n]
            newN = Node(n.val)
            visit[n] = newN
            for nei in n.neighbors:
                newN.neighbors.append(dfs(nei))
            return newN
        return dfs(node)

        