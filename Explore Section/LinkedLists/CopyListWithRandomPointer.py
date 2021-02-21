"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        tempDict = dict()

        newHead = temp = head

        while head:
            tempDict[head] = Node(head.val, None, None)
            head = head.next

        while temp:
            if temp.random:
                tempDict[temp].random = tempDict[temp.random]
            else:
                tempDict[temp].random = None
            if temp.next:
                tempDict[temp].next = tempDict[temp.next]
            else:
                tempDict[temp].next = None
            temp = temp.next

        return tempDict[newHead]
