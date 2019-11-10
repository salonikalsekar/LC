"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        tempdict = dict()

        newtemp = temp = head

        while head:
            tempdict[head] = Node(head.val, None, None)
            head = head.next

        while temp:
            if temp.random:
                tempdict[temp].random = tempdict[temp.random]
            else:
                tempdict[temp].random = None
            if temp.next:
                tempdict[temp].next = tempdict[temp.next]
            else:
                tempdict[temp].next = None

            temp = temp.next

        return tempdict[newtemp]

