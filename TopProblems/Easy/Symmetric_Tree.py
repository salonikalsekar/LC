# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        h = defaultdict(list)
        if not root:
            return True

        self.sym(root, 1, h)
        for k, v in h.items():
            if v[::] != v[::-1]:
                return False
        return True

    def sym(self, node, level, h):
        if node == None:
            h[level].append(None)
        else:
            h[level].append(node.val)
        if node:
            if node.left:
                self.sym(node.left, level + 1, h)
            else:
                self.sym(None, level + 1, h)
            if node.right:
                self.sym(node.right, level + 1, h)
            else:
                self.sym(None, level + 1, h)

        # Iterative
#         q = []
#         h = defaultdict(list)
#         if not root:
#             return True
#         q.append((root, 1))

#         while q:
#             node, level = q.pop(0)
#             if not node:
#                 h[level].append(None)
#             if node:
#                 h[level].append(node.val)
#                 if node.left:
#                     q.append((node.left, level + 1))
#                 else:
#                     q.append((None, level + 1))
#                 if node.right:
#                     q.append((node.right, level + 1))
#                 else:
#                     q.append((None, level + 1))

#         for k, v in h.items():
#             if v[::] != v[::-1]:
#                 return False

#         return True






