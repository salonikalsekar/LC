# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:
            return

        if head.next == None:
            return

        slow = head.next
        fast = head.next.next
        while fast != slow:
            if fast == None:
                return
            if fast.next == None:
                return

            fast = fast.next.next
            slow = slow.next
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast

