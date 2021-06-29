# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        h = defaultdict(list)
        if not root:
            return

        self.levelorder(root, 1, h)
        return h.values()

    def levelorder(self, node, level, h):
        if node:
            h[level].append(node.val)

            if node.left:
                self.levelorder(node.left, level + 1, h)
            if node.right:
                self.levelorder(node.right, level + 1, h)




