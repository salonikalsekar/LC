"""
# Definition for a Node
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import defaultdict


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return

        temp = defaultdict(list)

        self.bfs(root, 1, temp)
        for k, v in temp.items():
            j = 0

            while j < len(v):
                if j == len(v) - 1:
                    v[j].next = None
                else:
                    v[j].next = v[j + 1]

                j += 1

        return (root)

    def bfs(self, node, level, temp):

        if not node:
            return

        temp[level].append(node)

        self.bfs(node.left, level + 1, temp)
        self.bfs(node.right, level + 1, temp)

        return
