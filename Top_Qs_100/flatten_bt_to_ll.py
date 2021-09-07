class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = []

        stack.append(root)

        while stack:

            curr = stack.pop()

            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

            if stack:
                curr.right = stack[-1]
                curr.left = None