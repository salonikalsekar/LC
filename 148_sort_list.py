# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return
        if not head.next:
            return head

        fast = head
        slow = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        sec = slow.next
        slow.next = None

        l = self.sortList(head)
        r = self.sortList(sec)
        return self.mergeList(l, r)

    def mergeList(self, l, r):
        temp = res = ListNode(0)

        if not l or not r:
            return l or r

        while l and r:
            if l.val < r.val:
                temp.next = l
                l = l.next
            else:
                temp.next = r
                r = r.next

            temp = temp.next

        while l:
            temp.next = l
            l = l.next
            temp = temp.next

        while r:
            temp.next = r
            r = r.next
            temp = temp.next

        return res.next

