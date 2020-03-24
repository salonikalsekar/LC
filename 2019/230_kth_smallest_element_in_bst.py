# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.inorder(root)[k - 1]

    def inorder(self, root):
        if not root:
            return []

        left, right = [], []

        left = self.inorder(root.left)
        right = self.inorder(root.right)

        return left + [root.val] + right
