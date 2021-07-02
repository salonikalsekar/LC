# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def ispali(self, arr):
        l = 0
        r = len(arr) - 1

        while l < r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True

    def isPalindrome(self, head: ListNode) -> bool:
        res = []
        node = head

        while head:
            res.append(head.val)
            head = head.next

        return self.ispali(res)