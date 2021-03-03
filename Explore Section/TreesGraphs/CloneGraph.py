"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict, deque


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        temp = node
        seen = defaultdict(Node)
        if not node:
            return

        q = deque([node])

        while q:
            curr = q.popleft()
            if curr and curr not in seen:
                seen[curr] = Node(curr.val, None)
            tempN = []
            for i in curr.neighbors:
                if i not in seen:
                    seen[i] = Node(i.val, None)
                    q.append(i)
                tempN.append(seen[i])
            seen[curr].neighbors = tempN

        return seen[temp]

