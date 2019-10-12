# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp = ListNode(0)
        rev = self.reverseList(head, temp)
        res = True
        temp = temp.next
        while rev and temp:
            if rev.val == temp.val:
                rev = rev.next
                temp = temp.next
            else:
                res = False
                break
        return res

    def reverseList(self, node, temp):
        prev = None
        while node:
            nextNode = node.next
            node.next = prev
            temp.next = temp = ListNode(node.val)
            prev = node
            node = nextNode
        return prev

