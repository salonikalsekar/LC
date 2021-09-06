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
        res = []

        def preorder(node, res):
            if not node:
                res.append('None')
                return

            res.append(str(node.val))
            preorder(node.left, res)
            preorder(node.right, res)

            return

        if root:
            preorder(root, res)

        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        data = data.split(',')

        def build(n, data):
            if n == 'None':
                return

            node = TreeNode(n)
            node.left = build(data.pop(0), data)
            node.right = build(data.pop(0), data)
            return node

        return build(data.pop(0), data)