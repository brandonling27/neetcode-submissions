# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkTree(root, root2):
            if (not root and root2) or (not root2 and root):
                return False
            if root is None and root2 is None:
                return True
            if root.val != root2.val:
                return False
            return checkTree(root.left, root2.left) and checkTree(root.right, root2.right)
       
        if checkTree(root, subRoot):
            return True
        if root.left:
            return self.isSubtree(root.left, subRoot)
        if root.right: 
            return self.isSubtree(root.right, subRoot)
        return False