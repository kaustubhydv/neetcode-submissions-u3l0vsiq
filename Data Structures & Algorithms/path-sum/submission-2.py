# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root, curr_sum):
            if not root:
                return
            curr_sum += root.val
            if curr_sum == targetSum and not root.left and not root.right:
                return True
            if helper(root.left, curr_sum):
                return True
            if helper(root.right, curr_sum):
                return True
        if helper(root, 0):
            return True
        return False
            

        

       
            
        