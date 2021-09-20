class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        def traverse(node, val):
            l = True
            r = True
            if node and node.val != val:
                return False

            if node.left:
                l = traverse(node.left, val)

            if node.right:
                r = traverse(node.right, val)

            return l and r

        if root:
            return traverse(root, root.val)
