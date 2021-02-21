# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        temp = dict()

        while headA or headB:
            if headA:
                if headA not in temp:
                    temp[headA] = headA.val
                else:
                    return headA
                headA = headA.next
            if headB:
                if headB not in temp:
                    temp[headB] = headB.val
                else:
                    return headB
                headB = headB.next

        return
