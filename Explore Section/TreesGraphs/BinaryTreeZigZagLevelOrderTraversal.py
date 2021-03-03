# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        temp = defaultdict(list)
        res = []
        if not root:
            return
        self.bfs(root, 1, temp)
        for k, v in temp.items():
            if k % 2 == 0:
                res.append(v[::-1])
            else:
                res.append(v)

        return res

    def bfs(self, node, level, temp):
        if not node:
            return

        temp[level].append(node.val)
        self.bfs(node.left, level + 1, temp)
        self.bfs(node.right, level + 1, temp)

        return
