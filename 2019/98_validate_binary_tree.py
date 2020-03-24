# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def check(node, lower=float('-inf'), upper=float('inf')):

            if not node:
                return True

            if node.val <= lower or node.val >= upper:
                return False

            if not check(node.right, node.val, upper):
                return False

            if not check(node.left, lower, node.val):
                return False

            return True

        return check(root)

#         if not root:
#             return True

#         if not root.left and not root.right:
#             return (root, True)
#         left, right = tuple(), tuple()
#         if root.left:
#             left= self.isValidBST(root.left)
#         if root.right:
#             right= self.isValidBST(root.right)

#         if left and right:
#             ans = False
#             nodel, validityl = left
#             noder, validityr = right
#             if validityl and validityr:
#                 if nodel.val < root.val and noder.val > root.val:
#                     print("haha")
#                     return (root, True)
#                 else:
#                     return False
#             return False


#         if left:
#             node, validity = left
#             if validity:
#                 if node.val < root.val:
#                     return (root, True)
#                 else:
#                     return False

#             return False

#         if right:
#             node, validity = right

#             if validity:
#                 if node.val > root.val:
#                     return (root, True)
#                 else:
#                     return False

#             return False