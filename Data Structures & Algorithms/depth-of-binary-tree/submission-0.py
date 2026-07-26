# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 1
        return self.getDepth(root, 1)
    
    def getDepth(self, root, depth):
        if root is None:
            return depth - 1
        return max(self.getDepth(root.left, depth+1), self.getDepth(root.right, depth+1))