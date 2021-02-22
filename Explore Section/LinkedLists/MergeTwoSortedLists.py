# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        newHead = head = ListNode(-1)

        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next

        if l1:
            head.next = l1
        else:
            head.next = l2

        return newHead.next
#         if not l1:
#             return l2
#         if not l2:
#             return l1

#         head = curr = ListNode(0)
#         temp = []
#         while l1 or l2:
#             if l1:
#                 temp.append(l1.val)
#                 l1 = l1.next
#             if l2:
#                 temp.append(l2.val)
#                 l2 = l2.next
#         i=0
#         sortedTemp = sorted(temp)
#         while i < len(sortedTemp):
#             print(sortedTemp[i])
#             head.next = ListNode(sortedTemp[i])
#             head = head.next
#             i+=1
#         return curr.next