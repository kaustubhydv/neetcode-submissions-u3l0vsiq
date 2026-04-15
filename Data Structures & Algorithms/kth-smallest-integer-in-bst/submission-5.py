# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
            res = []
            if not root or k <= 0:
                return None
            def inorder(root):
                if not root:
                    return None
                # if len(res) == k:
                #     return
                else:
                    inorder(root.left)
                    res.append(root.val)
                    inorder(root.right)
            inorder(root)
            return res[k-1]
        

        