# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import defaultdict


# Floyd's Cycle Algorithm
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False

            slow = slow.next
            fast = fast.next.next
        return True

# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         temp = defaultdict(int)

#         while head != None:
#             if head not in temp:
#                 temp[head] = head.next
#                 head = head.next
#             else:
#                 return True

#         return False

