# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def preorder(node):
    if not node:
        return []
    return [node] + preorder(node.left) + preorder(node.right)


class Solution:
    def flatten(self, root: TreeNode) -> None:

        if not root:
            return

        flat = preorder(root)

        root = flat.pop(0)
        temp = root
        while flat:
            temp.right = flat.pop(0)
            temp.left = None
            temp = temp.right

