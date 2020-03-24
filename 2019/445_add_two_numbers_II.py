# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        final = []

        while l1 or l2:
            if l1:
                stack1.append(l1.val)
                l1 = l1.next
            if l2:
                stack2.append(l2.val)
                l2 = l2.next

        carry = 0

        while stack1 or stack2:
            if stack1:
                carry += stack1.pop()
            if stack2:
                carry += stack2.pop()
            carry, val = divmod(carry, 10)
            final.append(val)
        if carry:
            final.append(carry)

        res = temp = ListNode(final.pop())

        while final:
            node = ListNode(final.pop())
            temp.next = node
            temp = temp.next

        return res

