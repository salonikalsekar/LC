# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for curr in lists:
            while curr:
                heapq.heappush(heap, curr.val)
                curr = curr.next

        res = finalList = ListNode(0)

        while heap:
            finalList.next = ListNode(heapq.heappop(heap))
            finalList = finalList.next

        return res.next