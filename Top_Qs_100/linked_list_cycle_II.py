#         self.next = None
from collections import defaultdict


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        h = defaultdict(ListNode)
        if head:
            temp = head

            while head:
                if head in h:
                    return head
                else:
                    h[head] = head.val
                head = head.next

        return