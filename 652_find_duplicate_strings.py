# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if not root:
            return []

        self.mapping = {}
        self.res = []
        self.traverse(root)
        return (self.res)

    def traverse(self, node):

        if node:
            temp = str(node.val) + '-' + self.traverse(node.left) + '-' + self.traverse(node.right)

            c = self.mapping.get(temp, 0)
            if c == 1:
                self.res.append(node)

            self.mapping[temp] = c + 1

            return temp

        else:
            return "#"





