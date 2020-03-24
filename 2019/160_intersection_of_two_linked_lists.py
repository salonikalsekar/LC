# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):

        visited = set()

        while headA:

            if headA in visited:
                return headA
            else:
                visited.add(headA)
            headA = headA.next

        while headB:
            if headB in visited:
                return headB
            else:
                visited.add(headB)

            headB = headB.next

        return
