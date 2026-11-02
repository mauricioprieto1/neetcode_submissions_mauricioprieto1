# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        while queue:
            curr = queue.popleft()
            curr.left = curr.right
            curr.right = curr.left
            if curr.left: queue.append(root.left)
            if curr.right: queue.append(root.right)
        return root



