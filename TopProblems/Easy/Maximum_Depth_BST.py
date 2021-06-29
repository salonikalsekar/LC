# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return self.maxDep(root, 1)

    def maxDep(self, node, level):
        if not node:
            return level - 1
        l = self.maxDep(node.left, level + 1)
        r = self.maxDep(node.right, level + 1)
        return max(l, r)

