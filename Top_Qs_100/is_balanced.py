class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def isBal(root):
            if not root:
                return True, -1

            islbal, left = isBal(root.left)
            isrbal, right = isBal(root.right)

            if not islbal or not isrbal:
                return False, 0

            return (abs(left - right) < 2, max(left, right) + 1)

        isbal, height = isBal(root)
        return isbal