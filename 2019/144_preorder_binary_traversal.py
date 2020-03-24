# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        stack = []
        final = []
        stack.append((root, False))

        while stack:

            curr, visited = stack.pop()
            if curr:
                if visited:
                    final.append(curr)

                else:
                    stack.append((curr.right, False))
                    stack.append((curr.left, False))
                    stack.append((curr.val, True))

        return final


