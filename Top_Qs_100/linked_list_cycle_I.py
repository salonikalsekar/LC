from collections import defaultdict


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        h = defaultdict(ListNode)
        if head:
            temp = head

            while head:
                if head in h:
                    return True
                else:
                    h[head] = head.val
                head = head.next

        return False