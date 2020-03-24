# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        curr = head
        while head != None:
            count += 1
            head = head.next

        mid = count // 2
        print("mid", mid)

        count1 = 0
        head = curr
        while head != None:
            print(count1)
            if count1 == mid:
                return head

            else:
                count1 += 1
                head = head.next