# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        res = result = ListNode(-1)
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next

        while heap:
            result.next = ListNode(heapq.heappop(heap))
            result = result.next

        return res.next