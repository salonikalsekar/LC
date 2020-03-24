"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque
from collections import defaultdict


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        seen = defaultdict(Node)
        temp = node
        q = deque([node])

        while q:
            curr = q.popleft()
            if curr not in seen:
                seen[curr] = Node(curr.val, None)

            tempN = []
            for i in curr.neighbors:
                if i not in seen:
                    q.append(i)
                    seen[i] = Node(i.val, None)
                tempN.append(seen[i])

            seen[curr].neighbors = tempN

        return seen[temp]
