"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

from collections import defaultdict


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head:
            h = defaultdict(Node)

            temp = curr = head

            while head:
                h[head] = Node(head.val)
                head = head.next

            while temp:
                if temp.next:
                    h[temp].next = h[temp.next]
                else:
                    h[temp].next = None

                if temp.random:
                    h[temp].random = h[temp.random]
                else:
                    h[temp].random = None

                temp = temp.next

            return h[curr]
