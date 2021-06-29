# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validateTree(root)

    def validateTree(self, root, upper=float('inf'), lower=float('-inf')):
        if not root:
            return True
        if root:
            if root.val >= upper or root.val <= lower:
                return False

            return self.validateTree(root.left, root.val, lower) and self.validateTree(root.right, upper, root.val)




