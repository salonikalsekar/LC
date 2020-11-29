# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        stack.append((root, float('-inf'), float(inf)))
        while stack:
            curr, lower, upper = stack.pop()
            if curr:
                if curr.val <= lower or curr.val >= upper:
                    return False

                stack.append((curr.left, lower, curr.val))
                stack.append((curr.right, curr.val, upper))

        return True
