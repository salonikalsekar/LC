# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
from collections import defaultdict


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        # Recursively

        if not root:
            return

        temp = defaultdict(list)

        self.bfs(root, 1, temp)
        return temp.values()

    def bfs(self, node, level, temp):

        if not node:
            return

        temp[level].append(node.val)

        self.bfs(node.left, level + 1, temp)
        self.bfs(node.right, level + 1, temp)

        return
        # Iteratively
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:

#         if not root:
#             return
#         temp = defaultdict(list)

#         q = deque()

#         q.append((root, 1))

#         while q:

#             node, level = q.popleft()

#             temp[level].append(node.val)
#             if node.left:
#                 q.append((node.left, level+1))
#             if node.right:
#                 q.append((node.right, level+1))


#         return temp.values()
