# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.createBST(nums)

    def createBST(self, nums):
        if nums:
            i = (len(nums) // 2)

            n = TreeNode(nums[i])
            n.left = self.createBST(nums[:i])
            n.right = self.createBST(nums[i + 1:])

            return n