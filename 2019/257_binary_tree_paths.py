# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return
        prev = []
        result = self.path(root, prev)
        final = []

        for i in result:
            finalStr = ""
            for j in i:
                finalStr += str(j) + "->"
            final.append(finalStr[:-2])

        return final

    def path(self, node, prev):
        res = []
        if not node.left and not node.right:
            return [prev + [node.val]]

        left, right = [], []
        if node.left:
            left = self.path(node.left, prev + [node.val])
        if node.right:
            right = self.path(node.right, prev + [node.val])

        if left:
            for i in left:
                res.append(i)

        if right:
            for j in right:
                res.append(j)
        return res



