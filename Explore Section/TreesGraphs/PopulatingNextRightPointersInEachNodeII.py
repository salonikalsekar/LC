"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
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
            i = 0
            while i < len(v):
                if i == len(v) - 1:
                    v[i].next = None
                else:
                    v[i].next = v[i + 1]
                i += 1
        return root

    def bfs(self, node, level, temp):
        if not node:
            return []
        temp[level].append(node)
        self.bfs(node.left, level + 1, temp)
        self.bfs(node.right, level + 1, temp)
        return