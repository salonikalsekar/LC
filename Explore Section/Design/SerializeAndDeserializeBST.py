# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        def preorder(root):
            left = []
            right = []
            if not root:
                return ['None']

            left = preorder(root.left)
            right = preorder(root.right)

            return [root.val] + left + right

        return ','.join([str(i) for i in preorder(root)])

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return

        nodes = data.split(',')
        node = nodes.pop(0)

        def build(node, nodes):
            if node == 'None':
                return
            else:
                treeNode = TreeNode(node)
                treeNode.left = build(nodes.pop(0), nodes)
                treeNode.right = build(nodes.pop(0), nodes)

                return treeNode

        return build(node, nodes)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans