# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:

        uniVal = root.val

        return self.traverseTree(root, uniVal)

    def traverseTree(self, root, uniVal):
        if root.val != uniVal:
            return False

        left, right = True, True
        if root.left:
            left = self.traverseTree(root.left, uniVal)

        if root.right:
            right = self.traverseTree(root.right, uniVal)

        return left and right

