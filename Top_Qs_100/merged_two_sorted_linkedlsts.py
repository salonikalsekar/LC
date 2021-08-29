class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = newNode = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = ListNode(l1.val)
                temp = temp.next
                l1 = l1.next

            else:
                temp.next = ListNode(l2.val)
                temp = temp.next
                l2 = l2.next

        if l1:
            temp.next = l1

        if l2:
            temp.next = l2

        return newNode.next