# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        else:
            queue = []
            queue.append((root, 1))

            while queue:
                curr, depth = queue.pop(0)

                if curr:
                    children = [curr.left, curr.right]
                    if not any(children):
                        if len(queue) == 0:
                            return depth
                    for i in children:
                        if i:
                            queue.append((i, depth + 1))