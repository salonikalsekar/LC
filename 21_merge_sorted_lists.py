# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = final = ListNode(0)
        while l1 or l2:
            if l1 == None:
                final.next = l2
                break;
            elif l2 == None:
                final.next = l1
                break;
            elif l1.val < l2.val:
                final.next = final = ListNode(l1.val)
                l1 = l1.next
            else:
                final.next = final = ListNode(l2.val)
                l2 = l2.next

        return head.next
