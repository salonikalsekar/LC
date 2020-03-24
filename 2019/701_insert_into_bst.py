# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        newNode = TreeNode(val)

        if not root:
            root = newNode

        if val < root.val:
            if root.left:
                self.insertIntoBST(root.left, val)
            else:
                root.left = newNode

        elif val > root.val:
            if root.right:
                self.insertIntoBST(root.right, val)
            else:
                root.right = newNode

        return root

