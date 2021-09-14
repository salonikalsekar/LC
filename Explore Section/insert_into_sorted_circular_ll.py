class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = head
        newN = Node(insertVal)

        if not head:
            newN.next = newN
            return newN

        while True:
            if head.val <= insertVal <= head.next.val:
                break

            if head.next.val < head.val:
                if head.val <= insertVal or insertVal <= head.next.val:
                    break

            head = head.next

            if node == head.next:
                break

        temp = head.next
        head.next = newN
        newN.next = temp
        return node