class LinkedListNode:
    def __init__(self, data):
        self.val = data
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """

        if not self.head:
            return -1
        else:
            i = 0
            curr = self.head
            while curr:
                if i == index:
                    return curr.val

                curr = curr.next
                i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newNode = LinkedListNode(val)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode = LinkedListNode(val)

        if not self.head:
            self.head = newNode
        else:
            curr = self.head
            while curr:
                if curr.next == None:
                    curr.next = newNode
                    break
                curr = curr.next

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        newNode = LinkedListNode(val)

        if index == 0:
            if self.head != None:
                temp = self.head
                self.head = newNode
                newNode.next = temp
            else:
                self.head = newNode

        else:
            i = 1
            curr = self.head

            while curr:
                if i == index:
                    temp = curr.next
                    curr.next = newNode
                    curr.next.next = temp
                    break
                i += 1
                curr = curr.next

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """

        curr = self.head
        i = 1

        if curr.next != None:
            if index == 0:
                temp = self.head.next
                self.head = temp
            else:
                while curr:

                    if index == i and curr.next != None:
                        curr.next = curr.next.next
                        break
                    i += 1
                    curr = curr.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)