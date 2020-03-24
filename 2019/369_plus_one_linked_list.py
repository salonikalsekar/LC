# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

        if not head: return

        def dfs(node):
            if not node:
                return 1

            carry = dfs(node.next)
            node.val += carry
            carry = node.val // 10
            node.val = node.val % 10
            return carry

        carryOne = dfs(head)
        if carryOne:
            newNode = ListNode(carryOne)
            newNode.next = head

            return newNode

        return head