# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return False
            if not root.left and not root.right and root.val == target:
                return True
            val1 = dfs(root.left)
            val2 = dfs(root.right)
            if val1:
                root.left = None
            if val2:
                root.right = None
            if not root.left and not root.right and root.val == target:
                return True
            else:
                return False
        dfs(root)
        if not root.left and not root.right and root.val == target:
                return None
        return root
        
        