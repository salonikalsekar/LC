# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = []
        s2 = []

        while l1 or l2:
            if l1:
                s1.append(l1.val)
                l1 = l1.next
            if l2:
                s2.append(l2.val)
                l2 = l2.next

        maxLen = max(len(s1), len(s2))
        i = 0
        carry = 0
        curr = None
        while i < maxLen:
            s1Val = 0
            s2Val = 0
            if s1:
                s1Val = s1.pop()
                carry += s1Val
            if s2:
                s2Val = s2.pop()
                carry += s2Val
            newHead = ListNode(carry % 10)
            newHead.next = curr
            curr = newHead
            carry = carry // 10
            i += 1
        if carry:
            newHead = ListNode(carry)
            newHead.next = curr
            curr = newHead
        return curr

