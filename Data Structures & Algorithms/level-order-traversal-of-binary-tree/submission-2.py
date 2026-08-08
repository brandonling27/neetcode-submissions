# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        if not root:
            return []
        nodes = deque([root])
        res = []
        level = []
        while nodes:
            n = len(nodes)
            for _ in range(n):
                curr = nodes.popleft()
                level.append(curr.val)
                if curr.left:
                    nodes.append(curr.left)
                if curr.right:
                    nodes.append(curr.right)
            res.append(level)
            level = []
        return res