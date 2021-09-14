from collections import defaultdict


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        h = defaultdict(list)

        def traverse(n, level, h):

            if n:
                h[level].append(n.val)
                if n.left:
                    traverse(n.left, level + 1, h)
                if n.right:
                    traverse(n.right, level + 1, h)

        res = []
        traverse(root, 1, h)
        for k, v in h.items():
            if k % 2 == 0:
                res.append(v[::-1])
            else:
                res.append(v)

        return res