# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import Counter
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        newtemp = []
        temp1 = temp = ListNode(0)
        while head:
            newtemp.append(head.val)
            head = head.next
        tempdict = Counter(newtemp)
        for k,v in tempdict.items():
            if v == 1:
                temp.next = temp = ListNode(k)
        return temp1.next