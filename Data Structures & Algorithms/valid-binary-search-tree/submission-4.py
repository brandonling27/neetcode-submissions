# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def doDfs(root, lower, upper):
            if not root:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            return doDfs(root.left, lower, root.val) and doDfs(root.right, root.val, upper)

        lower = float('-inf')
        upper = float('inf')
        return doDfs(root, lower, upper)
  


