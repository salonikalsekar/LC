# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.traverse(root)[1]

    def traverse(self, node):
        if not node:
            return 0, True

        l1, isBalL = self.traverse(node.left)
        l2, isBalR = self.traverse(node.right)

        if abs(l2 - l1) > 1:
            isBal = False
        else:
            isBal = True

        return (max(l1 + 1, l2 + 1), (isBal and isBalL and isBalR))