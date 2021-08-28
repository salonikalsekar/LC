# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        #         def inorderTraversal(res, root):
        #             if root.left:
        #                 inorderTraversal(res, root.left)
        #             res.append(root.val)
        #             if root.right:
        #                 inorderTraversal(res, root.right)

        #             return res
        #         res = []
        #         if root:
        #             inorderTraversal(res, root)

        #         return res

        stack = [(root, False)]
        res = []
        while stack:
            n, visited = stack.pop()

            if n:
                if visited:
                    res.append(n.val)
                else:
                    stack.append((n.right, False))
                    stack.append((n, True))
                    stack.append((n.left, False))

        return res