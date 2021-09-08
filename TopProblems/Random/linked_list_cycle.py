from collections import defaultdict


class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        h = defaultdict(ListNode)
        node = head
        while head:
            if head in h:
                return True
            else:
                h[head] = head

            head = head.next
        return False