# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inOrder(p, q):
            # if p is not None and q is None --> False
            # if q is not None and p is None --> False
            # if q and p and q.val != p.val --> False
            # inOrder(p.left, q.left)
            # inOrder (p.right, q.left)
            # return True
            if p is not None and q is None:
                print('p, no q: ', p.val)
                return False
            if q is not None and p is None:
                print('q, no p: ', q.val)
                return False
            if p and q:
                if p.val != q.val:
                    print('not the same')
                    return False
                return inOrder(p.left, q.left) and inOrder(p.right, q.right)
            return True
        return inOrder(p,q)

        