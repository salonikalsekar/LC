# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import defaultdict


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        stack = [(root, 1)]
        dicttemp = defaultdict(list)

        while stack:
            node, level = stack.pop()
            if not node:
                dicttemp[level].append(None)
                continue
            else:
                dicttemp[level].append(node.val)

            if node.left:
                stack.append((node.left, level + 1))
            else:
                stack.append((None, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
            else:
                stack.append((None, level + 1))

        for k, v in dicttemp.items():
            if v[:] != v[::-1]:
                return False

        return True




