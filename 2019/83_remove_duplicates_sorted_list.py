# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        newtemp = []
        while head:
            if head.val not in newtemp:
                newtemp.append(head.val)
            head = head.next

        temp1 = temp = ListNode(0)
        i = 0
        while i < len(newtemp):
            temp.next = temp = ListNode(newtemp[i])
            i += 1

        return temp1.next
