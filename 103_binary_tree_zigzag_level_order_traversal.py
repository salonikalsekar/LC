# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return

        temp = defaultdict(list)
        result = []
        self.bfs(root, temp, 1)

        for k, v in temp.items():
            if k % 2 != 0:
                result.append(v)
            else:
                result.append(v[::-1])

        return result

    def bfs(self, node, temp, level):

        if not node:
            return

        temp[level].append(node.val)
        self.bfs(node.left, temp, level + 1)
        self.bfs(node.right, temp, level + 1)

        return



