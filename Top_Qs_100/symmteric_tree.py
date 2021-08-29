from collections import defaultdict


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        temp = defaultdict(list)

        def symmetric(node, temp, level):
            if node:
                temp[level].append(node.val)
            else:
                temp[level].append(None)
            if node:
                if node.left:
                    symmetric(node.left, temp, level + 1)
                else:
                    symmetric(None, temp, level + 1)
                if node.right:
                    symmetric(node.right, temp, level + 1)
                else:
                    symmetric(None, temp, level + 1)
            return

        symmetric(root, temp, 1)
        for k, v in temp.items():
            if v != v[::-1]:
                return False

        return True