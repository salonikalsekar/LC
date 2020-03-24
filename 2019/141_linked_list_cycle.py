# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def hasCycle(self, head):
#
#         fast = slow = head
#         if head == None:
#             return False
#         while fast:
#             if fast.next:
#                 fast = fast.next.next
#             else:
#                 return False
#             if fast == slow:
#                 return True
#             slow = slow.next
#
#         return False


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return False
        else:
            seen = set()
            while head:
                if head in seen:
                    return True
                else:
                    seen.add(head)
                    head = head.next

            return False


