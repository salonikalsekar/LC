class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0

        node = h = ListNode(0)
        while l1 or l2:

            if l1:
                carry += l1.val
                l1 = l1.next

            if l2:
                carry += l2.val
                l2 = l2.next

            node.next = ListNode(carry % 10)
            carry = carry // 10
            node = node.next

        if carry:
            node.next = ListNode(carry % 10)

        return h.next