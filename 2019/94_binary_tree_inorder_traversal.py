# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         if not root:
#             return []

#         leftSubtree = self.inorderTraversal(root.left)
#         rightSubtree = self.inorderTraversal(root.right)

#         return leftSubtree + [root.val] + rightSubtree

# Iterative

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        final = []
        stack.append((root, False))

        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    final.append(cur.val)

                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))

        return final









