# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        res = []
        if root:
            queue.append(root)
        while len(queue) > 0:
            k = len(queue)
            for i in range(k):
                temp = queue.popleft()
                if i == k-1:
                    res.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        return res

        