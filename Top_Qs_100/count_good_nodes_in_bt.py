class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.total = 0

        def traverse(node, max_till_now):
            if node.val >= max_till_now:
                self.total += 1

            if node.left:
                traverse(node.left, max(max_till_now, node.val))
            if node.right:
                traverse(node.right, max(max_till_now, node.val))

        traverse(root, float('-inf'), )
        return self.total