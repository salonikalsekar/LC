# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.val == None or head.next == None:
            return
        curr1 = head
        curr = newlist = ListNode(0)
        count = 0
        while head != None:
            count += 1
            head = head.next

        count1 = 1
        idx = (count - n) + 1
        head = curr1
        while head != None:

            if count1 == idx:
                head = head.next
            else:
                newlist.next = newlist = ListNode(head.val)
                head = head.next
            count1 += 1

        return curr.next









