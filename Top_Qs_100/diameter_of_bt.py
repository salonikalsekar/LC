# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0

        def traverse(root):
            if not root:
                return 0

            dl = traverse(root.left)
            dh = traverse(root.right)

            self.d = max(self.d, dl + dh)

            return max(dl, dh) + 1

        traverse(root)
        return self.d