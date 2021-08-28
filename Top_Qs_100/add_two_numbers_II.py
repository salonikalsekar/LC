class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        arr2 = []

        while l1:
            arr1.append(l1.val)
            l1 = l1.next

        while l2:
            arr2.append(l2.val)
            l2 = l2.next

        arr1 = arr1[::-1]
        arr2 = arr2[::-1]
        i = 0
        j = 0
        final = []
        carry = 0
        while i < len(arr1) or j < len(arr2) or carry:

            if i < len(arr1):
                carry += arr1[i]
                i += 1

            if j < len(arr2):
                carry += arr2[j]
                j += 1

            final.append(carry % 10)
            carry = carry // 10

        newNode = node = ListNode(0)
        final = final[::-1]
        for i in final:
            newNode.next = ListNode(i)
            newNode = newNode.next

        return node.next