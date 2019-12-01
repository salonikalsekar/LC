# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        d = defaultdict(list)

        self.traverse(root, d)
        res = []
        for k, v in sorted(d.items()):
            res.append(v)

        return res

    def traverse(self, root, d):

        if not root:
            return

        q = [(root, 0)]

        while q:
            node, level = q.pop(0)
            d[level].append(node.val)
            if node.left:
                q.append((node.left, level - 1))
            if node.right:
                q.append((node.right, level + 1))

        return



