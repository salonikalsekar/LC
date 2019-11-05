# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left, right = sys.maxsize, sys.maxsize
        if root.left:
            left = self.minDepth(root.left)
        if root.right:
            right = self.minDepth(root.right)
        res = min(left, right) + 1

        return res


