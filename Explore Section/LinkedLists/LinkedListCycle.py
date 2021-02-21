# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import defaultdict


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        temp = defaultdict(int)

        while head != None:
            if head not in temp:
                temp[head] = head.next
                head = head.next
            else:
                return True

        return False

