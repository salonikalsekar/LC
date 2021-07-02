# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import defaultdict


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        h = defaultdict()

        node = head

        while head:
            if head not in h:
                h[head] = head.val
            else:
                return True
            head = head.next

        return False