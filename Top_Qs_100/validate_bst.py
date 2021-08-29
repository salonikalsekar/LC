class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(root, left=float('-inf'), right=float('inf')):
            if not root:
                return True

            if root.val <= left or root.val >= right:
                return False

            if not validate(root.left, left, root.val):
                return False
            if not validate(root.right, root.val, right):
                return False

            return True

        return validate(root)