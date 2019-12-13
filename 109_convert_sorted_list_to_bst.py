# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        res = []

        node = head

        if not head:
            return

        while head:
            res.append(head.val)
            head = head.next

        return self.treeFormation(res)

    def treeFormation(self, nodeList):

        if not nodeList:
            return

        mid = len(nodeList) // 2

        node = TreeNode(nodeList[mid])
        node.left = self.treeFormation(nodeList[:mid])
        node.right = self.treeFormation(nodeList[mid + 1:])

        return node
