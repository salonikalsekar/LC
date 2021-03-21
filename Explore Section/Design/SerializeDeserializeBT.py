# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def preorder(node):
            if not node:
                return ['None']

            left = []
            right = []

            left = preorder(node.left)
            right = preorder(node.right)

            return [node.val] + left + right

        return ','.join([str(i) for i in preorder(root)])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tree = data.split(',')

        def build(node, tree):
            if node == 'None':
                return
            treeNode = TreeNode(node)
            treeNode.left = build(tree.pop(0), tree)
            treeNode.right = build(tree.pop(0), tree)

            return treeNode

        return build(tree.pop(0), tree)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))