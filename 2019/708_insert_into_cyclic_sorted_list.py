# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val, next):
#         self.val = val
#         self.next = next
# """

# from collections import defaultdict
# class Solution:
#     def insert(self, head: 'Node', insertVal: int) -> 'Node':
#         if not head:
#             return Node(insertVal)

#         head1 = head
#         newdict = defaultdict(Node)

#         while head.val not in newdict:
#             newdict[head.val] = head
#             head = head.next

#         if max(newdict) <= insertVal or min(newdict) >= insertVal:
#             tempnode = newdict[max(newdict)]

#         else:
#             tempnode = Node(None)

#             for k in newdict.keys():
#                 if k <= insertVal:
#                     tempnode = newdict[k]

#         newnode = Node(insertVal)

#         temp1 = tempnode.next
#         tempnode.next = newnode
#         newnode.next = temp1

#         return head

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            return Node(insertVal, None)
        cur = head
        newNode = Node(insertVal)

        while True:
            nextNode = cur.next.val
            currNode = cur.val

            if (nextNode < currNode and (insertVal <= nextNode or insertVal >= currNode)) or (
                    currNode <= insertVal <= nextNode) or (cur.next == head):
                temp = cur.next
                cur.next = newNode
                newNode.next = temp
                return head
            cur = cur.next
        return head



