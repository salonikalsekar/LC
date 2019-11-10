# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if not head:
            return

        odd, even = head, head.next

        while even and even.next:
            temp = even.next
            even.next = even.next.next  # 2->4
            temp.next = odd.next  # 3->2
            odd.next = temp  # 1->3

            odd, even = odd.next, even.next

        return head
