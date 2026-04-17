# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum_arr = []
        def pathHelper(root, sum_arr):
            if not root:
                return False
            sum_arr.append(root.val)
            if not root.left and not root.right:
                if targetSum == sum(sum_arr):
                    return True
                else:
                    sum_arr.pop()
                    return False
            if pathHelper(root.left, sum_arr):
                return True
            if pathHelper(root.right, sum_arr):
                return True
            sum_arr.pop()
            return False
        return pathHelper(root, sum_arr)
            
        